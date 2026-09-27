from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.document import Document
from app.services.document_service import process_document


router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    strategy: str = Form("fixed"),
    db: Session = Depends(get_db),
):
    allowed_extensions = {".pdf", ".txt"}

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in allowed_extensions:
        raise ValueError(
            "Unsupported file type. Only .pdf and .txt files are allowed."
        )

    allowed_strategies = {"fixed", "sentence"}

    if strategy not in allowed_strategies:
        raise ValueError(
            "Invalid chunking strategy. Choose 'fixed' or 'sentence'."
        )

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        buffer.write(await file.read())

    document = Document(
        filename=file.filename,
        file_path=str(file_path),
        status="uploaded",
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    chunk_count = process_document(
        document,
        db,
        strategy=strategy,
    )

    return {
        "id": document.id,
        "filename": document.filename,
        "file_path": document.file_path,
        "status": document.status,
        "chunking_strategy": strategy,
        "chunk_count": chunk_count,
    }
