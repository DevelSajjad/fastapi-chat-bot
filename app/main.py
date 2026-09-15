from fastapi import FastAPI
from app.api.routes.users import router as user_routes

app = FastAPI()

app.include_router(user_routes)