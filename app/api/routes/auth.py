from fastapi import APIRouter, Depends
from  sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.auth import (RegisterRequest, UserResponse)
from app.services.auth_service import (
    register_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post('/registration', response_model= UserResponse)

def register(data:RegisterRequest, db:Session = Depends(get_db)):

    user = register_user(
        db,
        data.full_name,
        data.email,
        data.password
    )

    return user
