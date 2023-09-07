import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, ForeignKey


class PasoEntregaDB(Base):
    __tablename__ = 'pasos_entregas'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    paso_id = Column(UUID(as_uuid=True), ForeignKey('pasos.id'), nullable=False)
    entrega_id = Column(UUID(as_uuid=True), ForeignKey('entregas.id'), nullable=False)