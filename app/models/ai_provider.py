from sqlalchemy import (
    String,
    Integer,
    Boolean,
    Text,
    DateTime,
    Float
)

from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.database.base import Base

class AIProvider(Base):
    __tablename__ = "ai_providers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    name: Mapped[str] = mapped_column(
        String(100)
    )


    provider_type: Mapped[str] = mapped_column(
        String(50)
    )
    # openai, gemini, claude, ollama


    api_key: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


    base_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )


    model: Mapped[str] = mapped_column(
        String(100)
    )


    temperature: Mapped[float] = mapped_column(
        Float,
        default=0.7
    )


    max_tokens: Mapped[int] = mapped_column(
        Integer,
        default=2000
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )