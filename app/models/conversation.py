from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.database.base import Base



class Conversation(Base):

    __tablename__ = "conversations"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id")
    )


    provider_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("ai_providers.id")
    )


    title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )