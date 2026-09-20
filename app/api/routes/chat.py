from fastapi import (APIRouter, Depends)
from sqlalchemy.orm import Session
from app.database.dependency import get_db
from app.models.conversation import Conversation
from app.models.chat_message import ChatMessage
from app.schemas.chat import ConversationCreate, ChatRequest
from app.services.chat_service import send_message
from app.core.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/conversation")
def create_conversation(
    data:ConversationCreate,
    current_user:User = Depends(get_current_user),
    db:Session=Depends(get_db)
):

    conversation = Conversation(
        user_id=current_user.id, 
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