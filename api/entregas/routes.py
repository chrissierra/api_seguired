from fastapi import APIRouter
from starlette import status
from api.entregas.endpoints import EntregaAPI
from api.entregas.models import EntregaModel, EntregaModelListar

entregas = EntregaAPI()
entregas_router = APIRouter()
# Para listar todas las entregas
entregas_router.add_api_route(
    path='/entregas',
    endpoint=entregas.list,
    response_model=list[EntregaModelListar],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener una entrega específica por ID
entregas_router.add_api_route(
    path='/entregas/{id}',
    endpoint=entregas.get,
    response_model=EntregaModel,
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para crear una nueva entrega
entregas_router.add_api_route(
    path='/entregas',
    endpoint=entregas.create,
    response_model=EntregaModel,
    status_code=status.HTTP_201_CREATED,
    methods=['POST']
)

# Para actualizar una entrega existente
entregas_router.add_api_route(
    path='/entregas/{id}',
    endpoint=entregas.update,
    response_model=EntregaModel,
    status_code=status.HTTP_200_OK,
    methods=['PUT']
)

# Para eliminar una entrega
entregas_router.add_api_route(
    path='/entregas/{id}',
    endpoint=entregas.delete,
    response_model=EntregaModel,
    status_code=status.HTTP_200_OK,
    methods=['DELETE']
)



