from typing import List
import uuid
from fastapi.params import Depends
from api.tipo_productos.models import CreateTipoProducto, TipoProducto, UpdateTipoProducto
from repositories.tipo_producto_repository import TipoProductoRepository

class TipoProductoAPI:

    def list(self, TipoProductoRepository: TipoProductoRepository = Depends(TipoProductoRepository)) -> list[TipoProducto]:
        return TipoProductoRepository.get_tipos_producto()

    def get(self, id: uuid.UUID, TipoProductoRepository: TipoProductoRepository = Depends(TipoProductoRepository)) -> TipoProducto:
        return TipoProductoRepository.get_tipo_producto(id)
    
    def get_by_id_usuario(self, usuario_id: uuid.UUID, TipoProductoRepository: TipoProductoRepository = Depends(TipoProductoRepository)) -> List[TipoProducto]:
        return TipoProductoRepository.get_by_id_usuario(usuario_id)

    def create(self, tipo_producto: CreateTipoProducto, tipoProductoRepository: TipoProductoRepository = Depends(TipoProductoRepository)) -> TipoProducto:
        return tipoProductoRepository.create_tipo_producto(usuario_id=tipo_producto.usuario_id, tipo_producto=tipo_producto.tipo_producto)

    def update(self, id: uuid.UUID, tipo_producto: UpdateTipoProducto, tipoProductoRepository: TipoProductoRepository = Depends(TipoProductoRepository)) -> TipoProducto:
        return tipoProductoRepository.update_tipo_producto(id, tipo_producto)

    def delete(self, id: uuid.UUID, tipoProductoRepository: TipoProductoRepository = Depends(TipoProductoRepository)):
        return tipoProductoRepository.delete_tipo_producto(id)