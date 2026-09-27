from datetime import date, time

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
    )

    email: Mapped[str] = mapped_column(
        String(255),
    )

    interview_date: Mapped[date]

    interview_time: Mapped[time]

    