from typing import List
import uuid
from fastapi import Depends
from api.ventas.models import CreateVenta, CreateVentaResponse, UpdateVenta, Venta
from repositories.venta_repository import VentaRepository
from api.ventas.models import CantidadesPorVenta
from api.ventas.models import Fecha


class VentaAPI:

    def list(self, venta_repository: VentaRepository = Depends(VentaRepository)) -> list[Venta]:
        return venta_repository.get_ventas()

    def get(self, id: uuid.UUID, venta_repository: VentaRepository = Depends(VentaRepository)) -> Venta:
        return venta_repository.get_venta(id)
    
    def get_by_id_usuario(self, id_usuario: uuid.UUID, venta_repository: VentaRepository = Depends(VentaRepository)) -> Venta:
        return venta_repository.get_venta_by_id_usuario(id_usuario)

    def create(self, venta: CreateVenta, lista_productos: List, lista_cantidades: List[CantidadesPorVenta], entrega: Fecha, venta_repository: VentaRepository = Depends(VentaRepository)) -> CreateVentaResponse:
        return venta_repository.create_venta(venta, lista_productos, lista_cantidades, entrega)

    def update(self, id: uuid.UUID, venta: UpdateVenta, venta_repository: VentaRepository = Depends(VentaRepository)) -> Venta:
        return venta_repository.update_venta(id, venta)

    def delete(self, id: uuid.UUID, venta_repository: VentaRepository = Depends(VentaRepository)):
        return venta_repository.delete_venta(id)