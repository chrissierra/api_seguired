import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db.paso_entrega.models import PasoEntregaDB

class EntregaDB(Base):
    __tablename__ = 'entregas'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    ventas_id = Column(UUID(as_uuid=True), ForeignKey('ventas.id'))
    fecha = Column(String)
    pasos = relationship('PasoDB', secondary=PasoEntregaDB.__tablename__, back_populates='entregas')
    venta = relationship("VentaDB", back_populates="entregas", foreign_keys="[EntregaDB.ventas_id]")