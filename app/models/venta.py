from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base


class Sale(Base):
    __tablename__ = "sale"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("user.id",ondelete="CASCADE"))
    worth = Column(Integer)
    quatity = Column(Integer)