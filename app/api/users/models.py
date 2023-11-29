
from pydantic import BaseModel 

from typing import Optional
from datetime import datetime 

#User Model 
class User(BaseModel): #Schema 
    username:str
    password:str 
    name:str 
    family_name:str 
    address:Optional[str]
    phone_number:int 
    email:str 
    date_creation:datetime =datetime.now()

class UpdateUser(BaseModel): #Schema 
    username:str = None 
    password:str = None 
    name:str = None 
    family_name:str = None 
    address:str = None 
    phone_number:int = None 
    email:str = None 

class ShowUser(BaseModel):
    username:str 
    nombre:str 
    email:str 
    class Config():
        orm_mode = True 