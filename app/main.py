from fastapi import FastAPI

from app.database.connection import engine
from app.database.base import Base
from app.models import User

from app.api.routes.users import router as user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes)