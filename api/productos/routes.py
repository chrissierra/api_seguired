from fastapi import APIRouter
from starlette import status
from api.productos.endpoints import ProductoAPI
from api.productos.models import Producto


productos = ProductoAPI()  # Asumiendo que tienes una clase ProductoAPI que implementa los métodos
productos_router = APIRouter()
# Para listar todos los productos
productos_router.add_api_route(
    path='/productos',
    endpoint=productos.list,
    response_model=list[Producto],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener un producto específico por ID
productos_router.add_api_route(
    path='/productos/{id}',
    endpoint=productos.get,
    response_model=Producto,
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener un tipo de producto específico por ID
productos_router.add_api_route(
    path='/productos/by-user/{usuario_id}',
    endpoint=productos.get_by_id_usuario,
    response_model=list[Producto],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)


# Para crear un nuevo producto
productos_router.add_api_route(
    path='/productos',
    endpoint=productos.create,
    response_model=Producto,
    status_code=status.HTTP_201_CREATED,
    methods=['POST']
)

# Para actualizar un producto existente
productos_router.add_api_route(
    path='/productos/{id}',
    endpoint=productos.update,
    response_model=Producto,
    status_code=status.HTTP_200_OK,
    methods=['PUT']
)

# Para eliminar un producto
productos_router.add_api_route(
    path='/productos/{id}',
    endpoint=productos.delete,
    response_model=Producto,
    status_code=status.HTTP_200_OK,
    methods=['DELETE']
)
