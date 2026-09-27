import re

from app.services.llm_service import generate_answer


def detect_intent(message: str) -> str:
    text = message.lower().strip()

    # Booking-detail patterns
    booking_patterns = [
        r"\b[\w\.-]+@[\w\.-]+\.\w+\b",  # email
        r"\bmy name is\b",
        r"\bi am\b",
        r"\bi'm\b",
        r"\bname\b",
        r"\bemail\b",
        r"\bdate\b",
        r"\btime\b",
        r"\b\d{1,2}(:\d{2})?\s*(am|pm)\b",  # time
        r"\b(january|february|march|april|may|june|july|august|"
        r"september|october|november|december)\b",  # month
        r"\bbook\b",
        r"\bbooking\b",
        r"\bschedule\b",
        r"\binterview\b",
    ]

    for pattern in booking_patterns:
        if re.search(pattern, text):
            return "booking"

    # Use the LLM for messages that don't clearly match booking patterns.
    prompt = f"""
Classify the user's message into exactly one category:

- "booking" if the user wants to schedule or book an interview.
- "question" for all other messages.

Return ONLY one word:

booking

or

question

User message:
{text}
"""

    result = generate_answer(prompt).strip().lower()

    if result == "booking":
        return "booking"

    return "question"