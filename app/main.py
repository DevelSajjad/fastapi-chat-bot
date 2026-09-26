from fastapi import FastAPI
from app.api.routes.users import router as user_routes
from app.core.config import settings

from app.database.connection import engine
from app.database.base import Base
from app.models.user import User
from app.api.routes.auth import router as auth_routes
from app.api.routes.ai_provider import router as ai_provider_routes
from app.api.routes.chat import router as chat_routes
from app.api.routes.document import router as document_routes

app = FastAPI(
    title = settings.APP_NAME
)

# app.include_router(user_routes)

app.include_router(auth_routes)
app.include_router(ai_provider_routes)
app.include_router(chat_routes)
app.include_router(chat_routes)
app.include_router(document_routes)
