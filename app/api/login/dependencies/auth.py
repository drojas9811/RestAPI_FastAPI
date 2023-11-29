from sqlalchemy.orm import Session 
from app.api.users import models
from fastapi import HTTPException,status 
from app.core.security.password import Hash
from app.core.security.authentication import create_access_token

def auth_user(user,db:Session):

    user = db.query(models.User).filter(models.User.username==user.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"""User {user.username} doesn't exist. Invalid login ."""
        )
    
    if not Hash.verify_password(user.password, user.password):
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"""Invalid password """
            )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

            