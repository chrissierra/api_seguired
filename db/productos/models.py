
import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class ProductoDB(Base):
    __tablename__ = 'productos'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    tipo_producto_id = Column(UUID(as_uuid=True), ForeignKey('tipos_producto_a.id'))
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuarios.id'))  # Nueva columna
    nombre = Column(String)
    precio = Column(String)
    imagen = Column(String)
    tipo_producto = relationship("TipoProductoDB", back_populates="productos", foreign_keys="[ProductoDB.tipo_producto_id]")
    ventas = relationship('VentaDB', secondary='venta_producto', back_populates='productos')
    ventas_cantidad = relationship('ProductoVentaCantidadDB', back_populates='producto')
    usuario = relationship("UserDB", back_populates="productos")  # Nuevo atributo de relación
