from fastapi import APIRouter
from starlette import status
from api.pasos.endpoints import PasosAPI
from api.pasos.models import CreatePasos, PasosResponseModelListar


pasos = PasosAPI()  # Asumiendo que tienes una clase PasosAPI que implementa los métodos
pasos_router = APIRouter()
# Para listar todos los pasos
pasos_router.add_api_route(
    path='/pasos',
    endpoint=pasos.list,
    response_model=list[PasosResponseModelListar],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener un paso específico por ID
pasos_router.add_api_route(
    path='/pasos/{id}',
    endpoint=pasos.get,
    response_model=PasosResponseModelListar,
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para crear un nuevo paso
pasos_router.add_api_route(
    path='/pasos',
    endpoint=pasos.create,
    response_model=CreatePasos,
    status_code=status.HTTP_201_CREATED,
    methods=['POST']
)

# Para actualizar un paso existente
pasos_router.add_api_route(
    path='/pasos/{id}',
    endpoint=pasos.update,
    response_model=PasosResponseModelListar,
    status_code=status.HTTP_200_OK,
    methods=['PUT']
)

# Para eliminar un paso
pasos_router.add_api_route(
    path='/pasos/{id}',
    endpoint=pasos.delete,
    response_model=PasosResponseModelListar,
    status_code=status.HTTP_200_OK,
    methods=['DELETE']
)


