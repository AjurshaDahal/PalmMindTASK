from app.services.vector_service import initialize_collection, client, COLLECTION_NAME


initialize_collection()

collections = client.get_collections().collections

print("Qdrant initialized successfully!")
print("Collections:")

for collection in collections:
    print("-", collection.name)

print(f"\nTarget collection: {COLLECTION_NAME}")
