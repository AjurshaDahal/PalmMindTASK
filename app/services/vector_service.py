




from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


COLLECTION_NAME = "document_chunks"
VECTOR_SIZE = 384

client = QdrantClient(path="./qdrant_data")


def initialize_collection() -> None:
    collections = client.get_collections().collections

    collection_names = [collection.name for collection in collections]

    if COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )


def store_embedding(
    chunk_id: int,
    embedding: list[float],
    chunk_text: str,
    document_id: int,
) -> None:
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=chunk_id,
                vector=embedding,
                payload={
                    "document_id": document_id,
                    "chunk_text": chunk_text,
                },
            )
        ],
    )
    