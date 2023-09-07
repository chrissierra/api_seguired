
from pydantic import BaseModel
from uuid import UUID

from api.tipo_productos.models import TipoProducto


class Producto(BaseModel):
    id: UUID
    tipo_producto_id: UUID
    nombre: str
    precio: str
    imagen: str
    tipo_producto: TipoProducto

    class Config:
        orm_mode = True


class CreateProducto(BaseModel):
    tipo_producto_id: UUID
    usuario_id: UUID
    nombre: str
    precio: str
    imagen: str

class UpdateProducto(BaseModel):
    tipo_producto_id: UUID
    nombre: str
    precio: str
    imagen: str

""" class Producto(BaseModel):
    id: UUID
    tipo_producto_id: UUID
    nombre: str
    precio: str
    imagen: str    

    class Config:
        orm_mode = True """

