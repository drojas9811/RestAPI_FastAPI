from fastapi import APIRouter,Depends,status 
from sqlalchemy.orm import Session 
from typing import List
from app.db.session import get_db
from app.api.login import Login
from app.api.login.dependencies import auth 
from fastapi.security import OAuth2PasswordRequestForm

login = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@login.post('/',status_code=status.HTTP_200_OK)
def login(user:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    auth_token = auth.auth_user(user, db)
    return auth_token
