from app.services.booking_extractor import extract_booking_details


message = """
Hi, I would like to schedule an interview.
My name is Ajursha Dahal and my email is ajursha@example.com.
I would like the interview on October 5 at 2 PM.
"""

details = extract_booking_details(message)

print("=== EXTRACTED BOOKING DETAILS ===")
print(details)
