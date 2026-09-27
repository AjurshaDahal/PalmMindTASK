from app.services.intent_service import detect_intent


messages = [
    "What machine learning skills does Ajursha have?",
    "I would like to schedule an interview.",
]

for message in messages:
    intent = detect_intent(message)

    print("Message:", message)
    print("Intent:", intent)
    print()
    