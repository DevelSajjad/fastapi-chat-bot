from sqlalchemy import (
    Integer,
    Text,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.database.base import Base



class ChatMessage(Base):

    __tablename__ = "chat_messages"



    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    conversation_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("conversations.id")
    )


    role: Mapped[str] = mapped_column(
        String(20)
    )
    # user / assistant


    content: Mapped[str] = mapped_column(
        Text
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )