
from pydantic import BaseModel
from uuid import UUID

from repositories.pasos_repository import PasosModel


class EntregaModel(BaseModel):
    ventas_id: UUID
    fecha: str
    class Config:
        orm_mode = True

class CreateEntrega(BaseModel):
    ventas_id: UUID
    fecha: str

class UpdateEntrega(BaseModel):
    ventas_id: UUID
    fecha: str


class EntregaModelListar(BaseModel):
    id: UUID
    ventas_id: UUID
    fecha: str
    class Config:
        orm_mode = True

class Entrega(BaseModel):
    ventas_id: UUID
    fecha: str
    pasos: list[PasosModel]
    """ pasos_id: UUID """
    class Config:
        orm_mode = True