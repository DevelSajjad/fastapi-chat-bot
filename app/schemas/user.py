from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: str
    password_hash: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True