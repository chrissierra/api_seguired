from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class Cliente(BaseModel):
    id: UUID
    nombre: str
    direccion: str
    rut: str
    latitud: float
    longitud: float
    email: Optional[str] = None

    class Config:
        orm_mode = True


class CreateCliente(BaseModel):
    nombre: str
    direccion: str
    rut: str
    latitud: float
    longitud: float
    email: Optional[str] = None
    usuario_id: UUID
    

class UpdateCliente(BaseModel):
    nombre: str
    direccion: str
    rut: str
    latitud: float
    longitud: float
    email: Optional[str] = None
    class Config:
        orm_mode = True

""" class Cliente(BaseModel):
    id: UUID
    nombre: str
    direccion: str
    rut: str
    latitud: float
    longitud: float
    email: Optional[str] = None
    class Config:
        orm_mode = True """