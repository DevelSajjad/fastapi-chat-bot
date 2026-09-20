from fastapi import APIRouter, Depends, HTTPException
from  sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.auth import (RegisterRequest, UserResponse, LoginRequest, TokenResponse)
from app.services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post('/registration', response_model= UserResponse)

def register(data:RegisterRequest, db:Session = Depends(get_db)):

    user = register_user(
        db,
        data.email,
        data.full_name,
        data.password
    )

    return user

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data:LoginRequest,
    db:Session=Depends(get_db)
):

    token = login_user(
        db,
        data.email,
        data.password
    )


    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token":token,

        "token_type":"bearer"
    }