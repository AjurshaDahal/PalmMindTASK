import re
from datetime import date, time


def validate_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return bool(re.match(pattern, email))


def validate_booking_details(
    details: dict,
) -> tuple[bool, str]:
    name = details.get("name")
    email = details.get("email")
    booking_date = details.get("date")
    booking_time = details.get("time")

    if not name:
        return False, "Please provide your name."

    if not email:
        return False, "Please provide your email address."

    if not validate_email(email):
        return False, "Please provide a valid email address."

    if not booking_date:
        return False, "Please provide your preferred interview date."

    if not booking_time:
        return False, "Please provide your preferred interview time."

    return True, "Booking details are valid."
