from typing import List
import uuid
from fastapi.params import Depends
from api.productos.models import CreateProducto, Producto, UpdateProducto
from repositories.producto_repository import ProductoRepository

class ProductoAPI:

    def list(self, producto_repository: ProductoRepository = Depends(ProductoRepository)) -> list[Producto]:
        return producto_repository.get_productos()

    def get(self, id: uuid.UUID, producto_repository: ProductoRepository = Depends(ProductoRepository)) -> Producto:
        return producto_repository.get_producto(id)
    
    def get_by_id_usuario(self, usuario_id: uuid.UUID, producto_repository: ProductoRepository = Depends(ProductoRepository)) -> List[Producto]:
        return producto_repository.get_producto_by_user_id(usuario_id)

    def create(self, producto: CreateProducto, producto_repository: ProductoRepository = Depends(ProductoRepository)) -> Producto:
        return producto_repository.create_producto(tipo_producto_id=producto.tipo_producto_id, nombre=producto.nombre, precio=producto.precio, imagen=producto.imagen, usuario_id=producto.usuario_id)

    def update(self, id: uuid.UUID, producto: UpdateProducto, producto_repository: ProductoRepository = Depends(ProductoRepository)) -> Producto:
        return producto_repository.update_producto(id, producto)

    def delete(self, id: uuid.UUID, producto_repository: ProductoRepository = Depends(ProductoRepository)):
        return producto_repository.delete_producto(id)