
from app.db.base import Base
from sqlalchemy import Column,Integer,String , Boolean,DateTime 
from datetime import datetime 
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String,unique=True)
    password = Column(String )
    name = Column(String)
    familyname = Column(String)
    address = Column(String)
    phonenumber = Column(String)
    email = Column(String, unique=True )
    creationdate = Column(DateTime, default=datetime.now, onupdate=datetime.now )
    state = Column(Boolean,default=False)
    sale = relationship("Sale",backref="user",cascade="delete,merge")