
from sqlalchemy import (String, Integer, DateTime, Boolean)
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    full_name: Mapped[String] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    role: Mapped[String] = mapped_column(
        String(50),
        default="user"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )