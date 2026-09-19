from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

def register_user(db:Session, email:str, full_name:str, password:str):

    hashed_password = hash_password(password)

    user = User(
        email=email,
        full_name=full_name,
        password_hash=hashed_password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user