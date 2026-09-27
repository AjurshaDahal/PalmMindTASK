from app.services.embedding_service import generate_embedding


text = "Python is a programming language."

embedding = generate_embedding(text)

print("Embedding generated successfully!")
print("Vector dimensions:", len(embedding))
print("First 5 values:", embedding[:5])