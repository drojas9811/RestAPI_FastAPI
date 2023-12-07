from os import getenv
from dotenv import load_dotenv
from pathlib import Path


class Settings:
    PROJECT_NAME: str = "FAST-API-PROJECT"
    PROJECT_VERSION: str = "1.0"
    POSTGRES_DB: str = getenv("NAME_DB")
    POSTGRES_USER: str = getenv("USER_DB")
    POSTGRES_PASSWORD: str = getenv("PASSWORD_DB")
    POSTGRES_SERVER: str = getenv("SERVER_DB")
    POSTGRES_PORT: str = getenv("PORT_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
