from datetime import date, time

from app.db.session import SessionLocal
from app.services.booking_service import create_booking


db = SessionLocal()

booking = create_booking(
    db=db,
    name="Ajursha Dahal",
    email="ajursha@example.com",
    interview_date=date(2026, 10, 5),
    interview_time=time(14, 0),
)

print("=== BOOKING CREATED ===")
print("ID:", booking.id)
print("Name:", booking.name)
print("Email:", booking.email)
print("Date:", booking.interview_date)
print("Time:", booking.interview_time)

db.close()
