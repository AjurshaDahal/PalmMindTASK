from app.services.booking_parser import (
    parse_booking_date,
    parse_booking_time,
)


booking_date = parse_booking_date("October 5, 2026")
booking_time = parse_booking_time("2 PM")

print("=== PARSED BOOKING ===")
print("Date:", booking_date)
print("Time:", booking_time)
