from dataclasses import Field
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from typing import Optional
from api.clientes.models import Cliente
from api.entregas.models import Entrega

from api.productos.models import Producto

""" class Producto(BaseModel):
    id: UUID
    tipo_producto_id: UUID
    nombre: str
    precio: str
    imagen: str    

    class Config:
        orm_mode = True

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

class Entrega(BaseModel):
    ventas_id: UUID
    fecha: str
    class Config:
        orm_mode = True """

class VentaResponse(BaseModel):
    id: UUID
    entrega_id: Optional[UUID]= None  # Este es opcional porque puede ser None
    cliente_id: UUID
    productos:Optional[str] = Producto
    cliente: Cliente
    entregas: list[Entrega]
    class Config:
        orm_mode = True


class Venta(BaseModel):
    id: UUID
    cliente_id: UUID
    """ entrega_id: Optional[UUID] = Field(None) """
    class Config:
        orm_mode = True

class CreateVenta(BaseModel):
    cliente_id: UUID
    """ entrega_id: Optional[UUID] = Field(None) """


class CreateVentaResponse(BaseModel):
    producto: list[Producto]
    cliente_id: UUID
    entrega_id:  Optional[str] = None


class UpdateVenta(BaseModel):
    cliente_id: UUID
    entrega_id: UUID

