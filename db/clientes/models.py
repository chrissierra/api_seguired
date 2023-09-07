import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class ClienteDB(Base):
    __tablename__ = 'clientes'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nombre = Column(String)
    direccion = Column(String)
    rut = Column(String)
    latitud = Column(Float)
    longitud = Column(Float)
    email = Column(String)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuarios.id'))
    ventas = relationship("VentaDB", back_populates="cliente", foreign_keys="[VentaDB.cliente_id]")
    usuario = relationship("UserDB", back_populates="clientes", foreign_keys="[ClienteDB.usuario_id]")
