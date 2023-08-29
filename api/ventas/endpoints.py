import uuid
from fastapi import Depends
from api.ventas.models import CreateVenta, CreateVentaResponse, UpdateVenta, Venta
from repositories.venta_repository import VentaRepository


class VentaAPI:

    def list(self, venta_repository: VentaRepository = Depends(VentaRepository)) -> list[Venta]:
        return venta_repository.get_ventas()

    def get(self, id: uuid.UUID, venta_repository: VentaRepository = Depends(VentaRepository)) -> Venta:
        return venta_repository.get_venta(id)

    def create(self, venta: CreateVenta, venta_repository: VentaRepository = Depends(VentaRepository)) -> CreateVentaResponse:
        return venta_repository.create_venta(venta)

    def update(self, id: uuid.UUID, venta: UpdateVenta, venta_repository: VentaRepository = Depends(VentaRepository)) -> Venta:
        return venta_repository.update_venta(id, venta)

    def delete(self, id: uuid.UUID, venta_repository: VentaRepository = Depends(VentaRepository)):
        return venta_repository.delete_venta(id)