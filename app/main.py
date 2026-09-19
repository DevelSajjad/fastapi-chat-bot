from fastapi import FastAPI
from app.api.routes.users import router as user_routes
from app.core.config import settings

from app.database.connection import engine
from app.database.base import Base
from app.models.user import User
from app.api.routes.auth import router as auth_routes


app = FastAPI(
    title = settings.APP_NAME
)

app.include_router(user_routes)

app.include_router(auth_routes)
