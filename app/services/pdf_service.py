from pathlib import Path

from pypdf import PdfReader


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    raise ValueError("Unsupported file type. Only .pdf and .txt are allowed.")
