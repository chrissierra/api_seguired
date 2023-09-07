import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, ForeignKey


class VentaProductoDB(Base):
    __tablename__ = 'venta_producto'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    venta_id = Column(UUID(as_uuid=True), ForeignKey('ventas.id'), nullable=False)
    producto_id = Column(UUID(as_uuid=True), ForeignKey('productos.id'), nullable=False)
