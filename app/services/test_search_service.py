from app.db.session import SessionLocal
from app.services.search_service import search_similar_chunks


db = SessionLocal()

query = "What programming and machine learning skills does the candidate have?"

results = search_similar_chunks(
    query=query,
    db=db,
    top_k=3,
)

print("=== SEARCH RESULTS ===")
print("Number of results:", len(results))

for i, result in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print("Score:", result.score)
    print("Document ID:", result.payload.get("document_id"))
    print("Text:", result.payload.get("chunk_text"))

db.close()
