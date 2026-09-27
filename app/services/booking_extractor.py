import json

from app.services.llm_service import generate_json


def extract_booking_details(
    message: str,
) -> dict:
    prompt = f"""
Extract interview booking information from the user's message.

Return a JSON object with exactly these four fields:

{{
    "name": string or null,
    "email": string or null,
    "date": string or null,
    "time": string or null
}}

If a field is not provided, use null.

Do not invent missing information.

User message:
{message}
"""

    response = generate_json(prompt)

    return json.loads(response)
