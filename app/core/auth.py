from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials   
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database.dependency import get_db
from app.models.user import User
from app.core.config import settings


SECRET_KEY = settings.AUTH_SECRET_KEY
ALGORITHM = "HS256"


# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="/auth/login"
# )

security = HTTPBearer()

def get_current_user(
    # token: str = Depends(oauth2_scheme),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if not user_id:
            raise Exception()

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()


    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    return user