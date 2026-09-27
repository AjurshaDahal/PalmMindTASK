from app.services.vector_service import COLLECTION_NAME, client


info = client.get_collection(COLLECTION_NAME)

print("Collection:", COLLECTION_NAME)
print("Vectors stored:", info.points_count)