from fastapi import APIRouter, Depends
from app.core.security import common_parameters
from sqlalchemy.orm import Session
from app.database.dependency import get_db
from app.models.user import User
from app.schemas.user import(
    UserCreate,
    UserResponse
)

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

@router.post('/',
      response_model= UserResponse      
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        email = user.email,
        password_has = user.password_hash
    )

    db.add(new_user)
    db.commit()
    db.refresh()

    return new_user

@router.get('/')
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return users

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User)\
        .filter(User.id == user_id)\
            .first()
    
    return user

@router.put('/{user_id}')
def update_user(user_id: int, email:str, db: Session = Depends(get_db)):
    user = db.query(User)\
        .filter(User.id == user_id)\
            .first()
    user.email = email

    db.commit()
    db.refresh(user)

    return user

@router.delete('/{user_id}')
def delete_user(user_id:int, db: Session = Depends(get_db)):
    user = db.query(User)\
        .filter(User.id == user_id)\
        .first()
    db.delete(user)

    db.commit()

    return {
        "message": "Deleted"
    }
