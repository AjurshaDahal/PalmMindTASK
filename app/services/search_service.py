from sqlalchemy.orm import Session

from app.services.embedding_service import generate_embedding
from app.services.vector_service import COLLECTION_NAME, client


def search_similar_chunks(
    query: str,
    db: Session,
    top_k: int = 3,
):
    query_embedding = generate_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k,
        with_payload=True,
    ).points

    return results