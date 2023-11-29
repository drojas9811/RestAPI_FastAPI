from fastapi import APIRouter,Depends,status 
from sqlalchemy.orm import Session 
from app.db.session import get_db
from app.api.login.repository.login import auth_user
from fastapi.security import OAuth2PasswordRequestForm

login = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@login.post('/',status_code=status.HTTP_200_OK)
def login_users(usuario:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    auth_token = auth_user(usuario, db)
    return auth_token
