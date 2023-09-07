import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db.paso_entrega.models import PasoEntregaDB

class PasosEstandarDB(Base):
    __tablename__ = 'pasos_estandar'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id_usuario = Column(UUID(as_uuid=True))
    nombre = Column(String)
    pasodb =  relationship("PasoDB", back_populates="pasos_estandar")

class PasoDB(Base):
    __tablename__ = 'pasos'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id_usuario = Column(UUID(as_uuid=True))
    tipo_producto_id = Column(UUID(as_uuid=True), ForeignKey('tipos_producto_a.id'), nullable=True)
    """ nombre_paso = Column(String) """
    id_paso_estandar = Column(UUID(as_uuid=True), ForeignKey('pasos_estandar.id'))
    ordinalidad = Column(String)
    caracteristicas = Column(String)
    entregas = relationship('EntregaDB', secondary=PasoEntregaDB.__tablename__, back_populates='pasos')
    tipo_producto = relationship("TipoProductoDB", back_populates="pasos")
    pasos_estandar =  relationship("PasosEstandarDB", back_populates="pasodb", foreign_keys="[PasoDB.id_paso_estandar]")