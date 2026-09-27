from datetime import date, time
from dateutil import parser


def parse_booking_date(value: str) -> date:
    parsed = parser.parse(value)

    return parsed.date()


def parse_booking_time(value: str) -> time:
    parsed = parser.parse(value)

    return parsed.time()
