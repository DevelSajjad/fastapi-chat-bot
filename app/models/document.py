from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column

from pgvector.sqlalchemy import Vector

from datetime import datetime

from app.database.base import Base



class Document(Base):

    __tablename__ = "documents"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    user_id: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )


    filename: Mapped[str] = mapped_column(
        String(255)
    )


    content: Mapped[str] = mapped_column(
        Text
    )


    embedding = mapped_column(
        Vector(384)
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )