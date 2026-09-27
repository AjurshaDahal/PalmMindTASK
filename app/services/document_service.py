from sqlalchemy.orm import Session

from app.models.document import Document, DocumentChunk
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embedding
from app.services.pdf_service import extract_text
from app.services.vector_service import initialize_collection, store_embedding


def process_document(
    document: Document,
    db: Session,
    strategy: str = "fixed",
) -> int:
    document.status = "processing"
    db.commit()

    initialize_collection()

    text = extract_text(document.file_path)

    chunks = chunk_text(
        text,
        strategy=strategy,
    )

    for chunk in chunks:
        embedding = generate_embedding(chunk)

        document_chunk = DocumentChunk(
            document_id=document.id,
            chunk_text=chunk,
            embedding=str(embedding),
        )

        db.add(document_chunk)
        db.flush()

        store_embedding(
            chunk_id=document_chunk.id,
            embedding=embedding,
            chunk_text=chunk,
            document_id=document.id,
        )

    document.status = "processed"
    db.commit()

    return len(chunks)