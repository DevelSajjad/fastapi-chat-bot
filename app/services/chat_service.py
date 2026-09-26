from sqlalchemy.orm import Session

from app.models.conversation import Conversation

from app.models.chat_message import ChatMessage

from app.models.ai_provider import AIProvider

from app.services.ai_provider_client import generate_ai_response
from app.services.document import rag_prompt




def send_message(
    db:Session,
    conversation_id:int,
    message:str
):


    # Get conversation
    conversation = db.query(
        Conversation
    ).filter(
        Conversation.id==conversation_id
    ).first()



    if not conversation:

        raise Exception(
            "Conversation not found"
        )


    # Get Provider

    provider = db.query(
        AIProvider
    ).filter(
        AIProvider.id==
        conversation.provider_id
    ).first()


    if not provider:

        raise Exception(
            "AI Provider not found"
        )


    # Save user message

    user_message = ChatMessage(
        conversation_id=conversation_id,

        role="user",

        content=message
    )


    db.add(user_message)

    db.commit()


    prompt = rag_prompt(db, message)

    # Generate AI response

    answer = generate_ai_response(
        provider,

        prompt
    )



    # Save AI message

    ai_message = ChatMessage(

        conversation_id=conversation_id,

        role="assistant",

        content=answer

    )


    db.add(ai_message)

    db.commit()



    return answer