
import uuid
from sqlalchemy import Column, Float
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from db.venta_producto.models import VentaProductoDB
from db.clientes.models import ClienteDB
from db.entregas.models import EntregaDB
from db.usuarios.models import UserDB
from db.productos.models import ProductoDB

class ProductoVentaCantidadDB(Base):
    __tablename__ = 'producto_venta_cantidad'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    cantidad = Column(Float)
    subtotal = Column(Float)
    venta_id = Column(UUID(as_uuid=True), ForeignKey('ventas.id'))
    producto_id = Column(UUID(as_uuid=True), ForeignKey('productos.id'), nullable=False)  # No debe ser nullable

    venta = relationship('VentaDB', back_populates='producto_venta_cantidad')
    producto = relationship('ProductoDB', back_populates='ventas_cantidad')

class VentaDB(Base):
    __tablename__ = 'ventas'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    cliente_id = Column(UUID(as_uuid=True), ForeignKey('clientes.id'))
    total = Column(Float)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuarios.id'))
    entrega_id = Column(UUID(as_uuid=True), ForeignKey('entregas.id'), nullable=True)
    productos = relationship(ProductoDB, secondary=VentaProductoDB.__tablename__, back_populates='ventas')
    cliente = relationship(ClienteDB, back_populates="ventas", foreign_keys=[cliente_id])
    usuario = relationship(UserDB, back_populates="ventas", foreign_keys=[usuario_id])
    entregas = relationship(EntregaDB, back_populates="venta", foreign_keys=[EntregaDB.ventas_id])
    producto_venta_cantidad = relationship('ProductoVentaCantidadDB', back_populates='venta')

