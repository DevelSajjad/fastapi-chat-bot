from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str
    DATABASE_URL: str
    AUTH_SECRET_KEY: str = "saktiman"
    ACCESS_TOKEN_EXPIRE_MINUTES: int=60

    class Config:
        env_file = '.env'

settings = Settings()