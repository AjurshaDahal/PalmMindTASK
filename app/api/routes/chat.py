from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.booking_service import process_booking_message
from app.services.intent_service import detect_intent
from app.services.rag_service import answer_question
from app.services.redis_service import get_booking_state



router = APIRouter()


class ChatRequest(BaseModel):
    conversation_id: str
    message: str


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    booking_state = get_booking_state(
        request.conversation_id,
    )

    if booking_state:
        intent = "booking"
    else:
        intent = detect_intent(request.message)

    if intent == "booking":
        response = process_booking_message(
            conversation_id=request.conversation_id,
            message=request.message,
            db=db,
        )

        return {
            "conversation_id": request.conversation_id,
            "intent": "booking",
            "answer": response,
        }

    answer = answer_question(
        question=request.message,
        db=db,
        conversation_id=request.conversation_id,
    )

    return {
        "conversation_id": request.conversation_id,
        "intent": "question",
        "answer": answer,
    }