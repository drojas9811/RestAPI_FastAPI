from fastapi import APIRouter,Depends,status 
from app.api.users.models import User,ShowUser,UpdateUser
from app.db.session import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.api.users.dependencies import user 
from app.core.security.authentication import get_current_user
users = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@users.get('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    data = user.obtener_usuarios(db)
    return data