from sqlalchemy.orm import Session 
from app.api.login import models
from fastapi import HTTPException,status 
from app.core.security.password import Hash
from app.core.security.jwt import create_access_token

def auth_user(usuario,db:Session):

    user = db.query(models.User).filter(models.User.username==usuario.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"""No existe el usuario con el username {usuario.username} por lo tanto no se realiza el login"""
        )
    
    if not Hash.verify_password(usuario.password, user.password):
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"""Contraseña incorrecta ! """
            )
    access_token = create_access_token(
        data={"sub": usuario.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

            