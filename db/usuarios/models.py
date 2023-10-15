import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class UserDB(Base):
    __tablename__ = 'usuarios'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nombre = Column(String)
    rut = Column(String)
    direccion = Column(String)
    logo = Column(String)
    email = Column(String, unique=True)
    clientes = relationship("ClienteDB", back_populates="usuario", foreign_keys="[ClienteDB.usuario_id]")
    productos = relationship("ProductoDB", back_populates="usuario")
    ventas = relationship("VentaDB", back_populates="usuario", foreign_keys="[VentaDB.usuario_id]")