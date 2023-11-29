from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5435/fastapi-database"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
localSession = sessionmaker(bind=engine,autocommit=False,autoflush=False)
def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()