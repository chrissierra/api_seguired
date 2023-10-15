from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from typing import Optional
from api.clientes.models import Cliente
from api.entregas.models import Entrega

from api.productos.models import Producto
from api.usuarios.models import User

class VentaProductoCantidad(BaseModel):
    id: UUID
    cantidad: float
    subtotal: float
    venta_id: UUID
    estado: Optional[str] = ''
    producto_id: UUID
    class Config:
        orm_mode = True

class VentaResponse(BaseModel):
    id: UUID
    entrega_id: Optional[UUID]= None  # Este es opcional porque puede ser None
    cliente_id: UUID
    usuario_id: UUID
    total: float
    productos: list[Producto]
    fecha_venta: Optional[date]
    cliente: Cliente
    estado: Optional[str] = ''
    entregas: list[Entrega]
    producto_venta_cantidad: list[VentaProductoCantidad]
    usuario: User
    class Config:
        orm_mode = True


class Venta(BaseModel):
    id: UUID
    cliente_id: UUID
    estado: Optional[str] = ''
    #fecha_venta: Optional[date]
    class Config:
        orm_mode = True

class CreateVenta(BaseModel):
    cliente_id: UUID
    usuario_id: UUID
    total: float
    estado: str


class CreateVentaResponse(BaseModel):
    producto: list[Producto]
    cliente_id: UUID
    fecha_venta: Optional[date]
    entrega_id:  Optional[str] = None
    estado: Optional[str] = ''


class UpdateVenta(BaseModel):
    cliente_id: UUID
    entrega_id: UUID
    estado: str

class CantidadesPorVenta(BaseModel):
    producto_id: UUID
    cantidad: float
    subtotal: float

class Fecha(BaseModel):
    fecha: str