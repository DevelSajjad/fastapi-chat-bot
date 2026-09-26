from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    email: EmailStr

    password: str = Field(
        min_length = 8
    )

    full_name: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    
class LoginRequest(BaseModel):

    email: EmailStr

    password: str


class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"