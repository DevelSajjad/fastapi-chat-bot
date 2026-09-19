from fastapi import FastAPI
from app.api.routes.users import router as user_routes
from app.core.config import settings

from app.database.connection import engine
from app.database.base import Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = settings.APP_NAME
)

app.include_router(user_routes)
