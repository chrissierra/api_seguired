from pydantic import BaseModel
from uuid import UUID



class CreateTipoProducto(BaseModel):
    usuario_id: UUID
    tipo_producto: str

class TipoProducto(BaseModel):
    id: UUID
    usuario_id: UUID
    tipo_producto: str
    class Config:
        orm_mode = True

class UpdateTipoProducto(BaseModel):
    usuario_id: UUID
    tipo_producto: str