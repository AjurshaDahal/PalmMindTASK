from app.db.session import SessionLocal
from app.services.rag_service import answer_question


db = SessionLocal()

conversation_id = "rag-test-001"

questions = [
    "What programming and machine learning skills does this person have?",
    "Which of those skills are related to computer vision?",
]

for question in questions:
    print(f"\n=== USER ===")
    print(question)

    answer = answer_question(
        question=question,
        db=db,
        conversation_id=conversation_id,
        top_k=3,
    )

    print("\n=== ASSISTANT ===")
    print(answer)

db.close()
