from typing import Optional

from pydantic import BaseModel, Field
from uuid import UUID

class PasosResponseModelListar(BaseModel):
    id: UUID
    id_usuario: UUID
    tipo_producto_id: UUID
    nombre_paso: str
    caracteristicas: str
    ordinalidad: str
    class Config:
        orm_mode = True


class CreatePasos(BaseModel):
    id_usuario: UUID
    tipo_producto_id: UUID
    nombre_paso: str
    caracteristicas: str
    ordinalidad: str

class UpdatePasos(BaseModel):
    id_usuario: UUID
    tipo_producto_id: UUID
    nombre_paso: str
    caracteristicas: str
    ordinalidad: str