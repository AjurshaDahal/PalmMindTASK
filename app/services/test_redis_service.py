from app.services.redis_service import (
    get_messages,
    save_message,
)


conversation_id = "test-conversation"

save_message(
    conversation_id,
    "user",
    "What skills does Ajursha have?",
)

save_message(
    conversation_id,
    "assistant",
    "Ajursha has Python, C, SQL, machine learning, and computer vision skills.",
)

messages = get_messages(conversation_id)

print("=== REDIS CHAT HISTORY ===")

for message in messages:
    print(message)

    from app.services.redis_service import (
    get_booking_state,
    save_booking_state,
)


booking_details = {
    "name": "Ajursha Dahal",
    "email": None,
    "date": None,
    "time": None,
}

save_booking_state(
    "booking-test-001",
    booking_details,
)

saved_details = get_booking_state(
    "booking-test-001",
)

print("\n=== BOOKING STATE ===")
print(saved_details)
