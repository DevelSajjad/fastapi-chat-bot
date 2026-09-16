from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password_hash: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True