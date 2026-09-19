from fastapi import (APIRouter, Depends)
from sqlalchemy.orm import Session
from app.database.dependency import get_db
from app.models.conversation import Conversation
from app.models.chat_message import ChatMessage
from app.schemas.chat import ConversationCreate, ChatRequest
from app.services.chat_service import send_message

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/conversation")
def create_conversation(
    data:ConversationCreate,
    db:Session=Depends(get_db)
):


    conversation = Conversation(
        user_id=1, # temporary
        provider_id=data.provider_id,
        title=data.title
    )

    db.add(conversation)

    db.commit()

    db.refresh(conversation)


    return conversation

@router.post("/message")
def chat_message(

    data:ChatRequest,

    db:Session=Depends(get_db)

):


    answer = send_message(

        db,

        data.conversation_id,

        data.message

    )


    return {

        "answer":answer

    }