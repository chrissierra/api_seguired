from fastapi import APIRouter
from starlette import status
from api.tipo_productos.endpoints import TipoProductoAPI
from api.tipo_productos.models import TipoProducto


tipo_productos = TipoProductoAPI()  # Asumiendo que tienes una clase TipoProductoAPI que implementa los métodos
tipo_productos_router = APIRouter()
# Para listar todos los tipos de productos
tipo_productos_router.add_api_route(
    path='/tipo_productos',
    endpoint=tipo_productos.list,
    response_model=list[TipoProducto],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener un tipo de producto específico por ID
tipo_productos_router.add_api_route(
    path='/tipo_productos/{id}',
    endpoint=tipo_productos.get,
    response_model=TipoProducto,
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener un tipo de producto específico por ID
tipo_productos_router.add_api_route(
    path='/tipo_productos/by-user/{usuario_id}',
    endpoint=tipo_productos.get_by_id_usuario,
    response_model=list[TipoProducto],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)


# Para crear un nuevo tipo de producto
tipo_productos_router.add_api_route(
    path='/tipo_productos',
    endpoint=tipo_productos.create,
    response_model=TipoProducto,
    status_code=status.HTTP_201_CREATED,
    methods=['POST']
)

# Para actualizar un tipo de producto existente
tipo_productos_router.add_api_route(
    path='/tipo_productos/{id}',
    endpoint=tipo_productos.update,
    response_model=TipoProducto,
    status_code=status.HTTP_200_OK,
    methods=['PUT']
)

# Para eliminar un tipo de producto
tipo_productos_router.add_api_route(
    path='/tipo_productos/{id}',
    endpoint=tipo_productos.delete,
    response_model=TipoProducto,
    status_code=status.HTTP_200_OK,
    methods=['DELETE']
)
