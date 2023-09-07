
from pydantic import BaseModel
from uuid import UUID
from typing import Optional
class PasosResponseModelListar(BaseModel):
    id: UUID
    id_usuario: UUID
    tipo_producto_id: UUID
    """ nombre_paso: str """
    caracteristicas: str
    ordinalidad: str
    class Config:
        orm_mode = True


class CreatePasos(BaseModel):
    id_usuario: UUID
    tipo_producto_id: Optional[UUID] = None
    """ nombre_paso: str """
    id_paso_estandar: UUID
    caracteristicas: str
    ordinalidad: str

class UpdatePasos(BaseModel):
    id_usuario: UUID
    tipo_producto_id: UUID
    """ nombre_paso: str """
    caracteristicas: str
    ordinalidad: str

class CreatePasoEstandar(BaseModel):
    id_usuario: UUID
    nombre: str


class PasoEstandar(BaseModel):
    id: UUID
    id_usuario: UUID
    nombre: str
    class Config:
        orm_mode = True
class Identificador(BaseModel):
    id: UUID
    class Config:
        orm_mode = True