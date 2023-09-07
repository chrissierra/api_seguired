from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class CreateUser(BaseModel):
    nombre: str
    direccion: str
    rut: str
    email: Optional[str] = None

class User(BaseModel):
    id: UUID
    nombre: str
    direccion: str
    rut: str
    email: Optional[str] = None

    class Config:
        orm_mode = True