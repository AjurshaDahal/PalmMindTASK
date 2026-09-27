from app.services.chunk_service import chunk_text
from app.services.pdf_service import extract_text


text = extract_text("uploads/AjurshaDahalCV (1).pdf")

fixed_chunks = chunk_text(
    text,
    strategy="fixed",
)

sentence_chunks = chunk_text(
    text,
    strategy="sentence",
)

print("=== FIXED-SIZE CHUNKING ===")
print("Total chunks:", len(fixed_chunks))

for i, chunk in enumerate(fixed_chunks[:2], start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)


print("\n\n=== SENTENCE CHUNKING ===")
print("Total chunks:", len(sentence_chunks))

for i, chunk in enumerate(sentence_chunks[:2], start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)
