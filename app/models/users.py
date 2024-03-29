
from pydantic import BaseModel 

from typing import Optional
from datetime import datetime 

#User Model 
class UserModel(BaseModel): #Schema 
    username:str
    password:str 
    name:str 
    family_name:str 
    address:Optional[str]
    phone_number:int 
    email:str 
    date_creation:datetime =datetime.now()

class UpdateUserModel(BaseModel): #Schema 
    username:str = None 
    password:str = None 
    name:str = None 
    familyname:str = None 
    address:str = None 
    phonenumber:int = None 
    email:str = None 

class ShowUserModel(BaseModel):
    id:int
    username:str 
    name:str 
    email:str 
    class Config():
        orm_mode = True 