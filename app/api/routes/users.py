from fastapi import APIRouter, Depends
from app.core.security import common_parameters

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get('/')
def get_users():
    return {
        "users"  : []
    }

@router.get("/{user_id}")

def get_user(user_id: int, params = Depends(common_parameters)):

    return {
        "id": user_id,
        "params": params
    }
