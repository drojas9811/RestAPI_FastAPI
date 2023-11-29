from sqlalchemy.orm import Session 
from app.api.users import models
from fastapi import HTTPException,status 
from app.core.security.password import Hash

def new_user(inUser,db:Session):
    dictUser = inUser.dict()
    try:
        newUser = models.User(
            username=dictUser["username"],
            password=Hash.hash_password(dictUser["password"]),
            nombre=dictUser["nombre"],
            apellido=dictUser["apellido"],
            direccion=dictUser["direccion"],
            telefono=dictUser["telefono"],
            correo=dictUser["correo"],
        )
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )

def get_user(user_id,db:Session):
    userFromDB = db.query(models.User).filter(models.User.id == user_id ).first()
    if not userFromDB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} doesn't exist."
        )
    return userFromDB

def delete_user(user_id,db:Session):
    userFromDB = db.query(models.User).filter(models.User.id == user_id )
    if not userFromDB.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} doesn't exist."
        )
    userFromDB.delete(synchronize_session=False)
    db.commit()
    return {"response":"deleting was successful"}

def get_allUsers(db:Session):
    data = db.query(models.User).all()
    return data

def update_user(user_id,updateUser,db:Session):
    userFromDB = db.query(models.User).filter(models.User.id == user_id )
    if not userFromDB.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} doesn't exist."
        )
    userFromDB.update(updateUser.dict( exclude_unset=True))
    db.commit()
    return {"response":"updating was successful"}