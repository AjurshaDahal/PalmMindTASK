import re


def fixed_size_chunking(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[str]:
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks


def sentence_chunking(
    text: str,
    sentences_per_chunk: int = 5,
) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    chunks = []

    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = " ".join(sentences[i:i + sentences_per_chunk])

        if chunk.strip():
            chunks.append(chunk.strip())

    return chunks


def chunk_text(
    text: str,
    strategy: str = "fixed",
) -> list[str]:
    if strategy == "fixed":
        return fixed_size_chunking(text)

    if strategy == "sentence":
        return sentence_chunking(text)

    raise ValueError(
        "Invalid chunking strategy. "
        "Choose 'fixed' or 'sentence'."
    )
