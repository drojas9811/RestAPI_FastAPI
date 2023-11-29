import os 
from dotenv import load_dotenv
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "FAST-API-PROJECT"
    PROJECT_VERSION:str = "1.0"
    POSTGRES_DB:str = "postgres"
    POSTGRES_USER:str = "postgres"
    POSTGRES_PASSWORD:str = "gobank"
    POSTGRES_SERVER:str = "db"
    POSTGRES_PORT:str = "5432"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()