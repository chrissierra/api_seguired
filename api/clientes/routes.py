from fastapi import APIRouter
from starlette import status
from api.clientes.endpoints import ClienteAPI
from api.clientes.models import Cliente


clientes = ClienteAPI()  # Asumiendo que tienes una clase ClienteAPI que implementa los métodos
clientes_router = APIRouter()
# Para listar todos los clientes
clientes_router.add_api_route(
    path='/clientes',
    endpoint=clientes.list,
    response_model=list[Cliente],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para listar todos los clientes by id usuario
clientes_router.add_api_route(
    path='/clientes-por-usuario/{id}',
    endpoint=clientes.list_by_id_usuario,
    response_model=list[Cliente],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener un cliente específico por ID
clientes_router.add_api_route(
    path='/clientes/{id}',
    endpoint=clientes.get,
    response_model=Cliente,
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para crear un nuevo cliente
clientes_router.add_api_route(
    path='/clientes',
    endpoint=clientes.create,
    response_model=Cliente,
    status_code=status.HTTP_201_CREATED,
    methods=['POST']
)

# Para actualizar un cliente existente
clientes_router.add_api_route(
    path='/clientes/{id}',
    endpoint=clientes.update,
    response_model=Cliente,
    status_code=status.HTTP_200_OK,
    methods=['PUT']
)

# Para eliminar un cliente
clientes_router.add_api_route(
    path='/clientes/{id}',
    endpoint=clientes.delete,
    response_model=Cliente,
    status_code=status.HTTP_200_OK,
    methods=['DELETE']
)


