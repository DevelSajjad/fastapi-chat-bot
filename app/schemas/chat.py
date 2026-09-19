from pydantic import BaseModel



class ConversationCreate(BaseModel):

    provider_id:int

    title:str | None = None




class ChatRequest(BaseModel):

    conversation_id:int

    message:str




class MessageResponse(BaseModel):

    id:int

    role:str

    content:str


    class Config:
        from_attributes=True