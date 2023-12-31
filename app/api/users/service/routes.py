from fastapi import APIRouter,Depends,status 
from app.models.users import ShowUserModel,UpdateUserModel
from app.db.session import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.api.users.repository.users import *
from app.core.security.authentication import get_current_user
users = APIRouter(
    prefix="/user",
    tags=["Users"]
)
User

@users.get('/',response_model=List[ShowUserModel],status_code=status.HTTP_200_OK)
def get_users(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    data = getAllUsers(db)
    return data

@users.post('/',status_code=status.HTTP_201_CREATED)
def create_user(usuario:UserModel,db:Session = Depends(get_db)):
    newUser(usuario,db)
    return {"response":"Creating was successful."}

@users.get('/{user_id}',response_model=ShowUserModel,status_code=status.HTTP_200_OK)
def get_user(user_id:int,db:Session = Depends(get_db)):
    returnedUser = getUser(user_id,db)
    return returnedUser

@users.delete('/{user_id}',status_code=status.HTTP_200_OK)
def delete_user(user_id:int,db:Session = Depends(get_db)):
    result = deleteUser(user_id, db)
    return result

@users.patch('/{user_id}',status_code=status.HTTP_200_OK)
def update_user(user_id:int,update_user:UpdateUserModel,db:Session = Depends(get_db)):
    result = updateUser(user_id,update_user, db)
    return result
