from datetime import date, time

from sqlalchemy.orm import Session

from app.models.booking import Booking


def create_booking(
    db: Session,
    name: str,
    email: str,
    interview_date: date,
    interview_time: time,
) -> Booking:
    booking = Booking(
        name=name,
        email=email,
        interview_date=interview_date,
        interview_time=interview_time,
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking

from app.services.booking_extractor import extract_booking_details
from app.services.booking_parser import (
    parse_booking_date,
    parse_booking_time,
)
from app.services.booking_validation import validate_booking_details
from app.services.redis_service import (
    clear_booking_state,
    get_booking_state,
    save_booking_state,
)


def process_booking_message(
    conversation_id: str,
    message: str,
    db: Session,
) -> str:
    existing_details = get_booking_state(
        conversation_id,
    )

    new_details = extract_booking_details(
        message,
    )

    booking_details = {
        "name": new_details.get("name") or existing_details.get("name"),
        "email": new_details.get("email") or existing_details.get("email"),
        "date": new_details.get("date") or existing_details.get("date"),
        "time": new_details.get("time") or existing_details.get("time"),
    }

    save_booking_state(
        conversation_id,
        booking_details,
    )

    required_fields = {
        "name": "your name",
        "email": "your email address",
        "date": "your preferred interview date",
        "time": "your preferred interview time",
    }

    missing_fields = [
        label
        for field, label in required_fields.items()
        if not booking_details.get(field)
    ]

    if missing_fields:
        return (
            "Sure! I still need "
            + ", ".join(missing_fields)
            + "."
        )

    is_valid, message_text = validate_booking_details(
        booking_details,
    )

    if not is_valid:
        return message_text

    try:
        interview_date = parse_booking_date(
            booking_details["date"],
        )

        interview_time = parse_booking_time(
            booking_details["time"],
        )
    except (ValueError, TypeError):
        return (
            "I couldn't understand the date or time. "
            "Please provide them in a format such as "
            "'October 5, 2026 at 2 PM'."
        )

    booking = create_booking(
        db=db,
        name=booking_details["name"],
        email=booking_details["email"],
        interview_date=interview_date,
        interview_time=interview_time,
    )

    clear_booking_state(
        conversation_id,
    )

    return (
        f"Your interview has been booked successfully. "
        f"Booking ID: {booking.id}. "
        f"Date: {booking.interview_date}. "
        f"Time: {booking.interview_time}."
    )