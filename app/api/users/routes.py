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

@users.post('/',status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario:User,db:Session = Depends(get_db)):
    user.crear_usuario(usuario,db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}

@users.get('/{user_id}',response_model=ShowUser,status_code=status.HTTP_200_OK)
def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
    usuario = user.obtener_usuario(user_id,db)
    return usuario

@users.delete('/{user_id}',status_code=status.HTTP_200_OK)
def eliminar_usuario(user_id:int,db:Session = Depends(get_db)):
    res = user.eliminar_usuario(user_id, db)
    return res 

@users.patch('/{user_id}',status_code=status.HTTP_200_OK)
def actualizar_user(user_id:int,updateUser:UpdateUser,db:Session = Depends(get_db)):
    res = user.actualizar_user(user_id,updateUser, db)
    return res 