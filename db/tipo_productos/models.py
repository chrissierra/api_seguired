import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class TipoProductoDB(Base):
    __tablename__ = 'tipos_producto_a'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    usuario_id = Column(UUID(as_uuid=True))
    tipo_producto = Column(String)
    productos = relationship("ProductoDB", back_populates="tipo_producto", foreign_keys="[ProductoDB.tipo_producto_id]")
    pasos = relationship("PasoDB", back_populates="tipo_producto")