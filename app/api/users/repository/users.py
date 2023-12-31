from sqlalchemy.orm import Session 
from app.models.users import *
from app.models.db import *
from fastapi import HTTPException,status 
from app.core.security.password import Hash
def newUser(inUser,db:Session):
    dictUser = inUser.dict()
    try:
        newUser = User(
            username=dictUser["username"],
            password=Hash.hash_password(dictUser["password"]),
            name=dictUser["name"],
            familyname=dictUser["family_name"],
            address=dictUser["address"],
            phonenumber=dictUser["phone_number"],
            email=dictUser["email"],
        )
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )

def getUser(user_id,db:Session):
    userFromDB = db.query(User).filter(User.id == user_id ).first()
    if not userFromDB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} doesn't exist."
        )
    return userFromDB

def deleteUser(user_id,db:Session):
    userFromDB = db.query(User).filter(User.id == user_id )
    if not userFromDB.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} doesn't exist."
        )
    userFromDB.delete(synchronize_session=False)
    db.commit()
    return {"response":"deleting was successful"}

def getAllUsers(db:Session):
    data = db.query(User).all()
    return data

def updateUser(user_id,update_user,db:Session):
    userFromDB = db.query(User).filter(User.id == user_id )
    if not userFromDB.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} doesn't exist."
        )
    userFromDB.update(update_user.dict( exclude_unset=True))
    db.commit()
    return {"response":"updating was successful"}