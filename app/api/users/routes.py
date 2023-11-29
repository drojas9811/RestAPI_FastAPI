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
def get_users(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    data = user.get_allUsers(db)
    return data

@users.post('/',status_code=status.HTTP_201_CREATED)
def create_user(usuario:User,db:Session = Depends(get_db)):
    user.new_user(usuario,db)
    return {"response":"Creating was successful."}

@users.get('/{user_id}',response_model=ShowUser,status_code=status.HTTP_200_OK)
def get_user(user_id:int,db:Session = Depends(get_db)):
    returnedUser = user.get_user(user_id,db)
    return returnedUser

@users.delete('/{user_id}',status_code=status.HTTP_200_OK)
def delete_user(user_id:int,db:Session = Depends(get_db)):
    result = user.delete_user(user_id, db)
    return result

@users.patch('/{user_id}',status_code=status.HTTP_200_OK)
def update_user(user_id:int,updateUser:UpdateUser,db:Session = Depends(get_db)):
    result = user.update_user(user_id,updateUser, db)
    return result