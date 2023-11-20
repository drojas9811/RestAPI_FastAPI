from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base


class Venta(Base):
    __tablename__ = "venta"
    id = Column(Integer,primary_key=True,autoincrement=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id",ondelete="CASCADE"))
    venta = Column(Integer)
    ventas_productos = Column(Integer)