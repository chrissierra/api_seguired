from typing import Optional

from pydantic import BaseModel, Field
from uuid import UUID


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
    """ pasos_id: UUID """
    class Config:
        orm_mode = True