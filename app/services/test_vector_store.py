from app.services.embedding_service import generate_embedding
from app.services.vector_service import (
    COLLECTION_NAME,
    client,
    initialize_collection,
    store_embedding,
)


initialize_collection()

text = "Python is a programming language used for machine learning."

embedding = generate_embedding(text)

store_embedding(
    chunk_id=999999,
    embedding=embedding,
    chunk_text=text,
    document_id=1,
)

points = client.retrieve(
    collection_name=COLLECTION_NAME,
    ids=[999999],
)

print("Vector stored successfully!")
print("Number of points retrieved:", len(points))

if points:
    print("Stored text:", points[0].payload["chunk_text"])
    print("Vector retrieved successfully!")
