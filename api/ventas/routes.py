from fastapi import APIRouter
from starlette import status

from api.ventas.endpoints import VentaAPI
from api.ventas.models import Venta, VentaResponse


ventas = VentaAPI()  # Asumiendo que tienes una clase VentaAPI que implementa los métodos
ventas_router = APIRouter()
# Para listar todas las ventas
ventas_router.add_api_route(
    path='/ventas',
    endpoint=ventas.list,
    response_model=list[VentaResponse],
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para obtener una venta específica por ID
ventas_router.add_api_route(
    path='/ventas/{id}',
    endpoint=ventas.get,
    response_model=VentaResponse,
    status_code=status.HTTP_200_OK,
    methods=['GET']
)

# Para crear una nueva venta
ventas_router.add_api_route(
    path='/ventas',
    endpoint=ventas.create,
    response_model=Venta,
    status_code=status.HTTP_201_CREATED,
    methods=['POST']
)

# Para actualizar una venta existente
ventas_router.add_api_route(
    path='/ventas/{id}',
    endpoint=ventas.update,
    response_model=Venta,
    status_code=status.HTTP_200_OK,
    methods=['PUT']
)

# Para eliminar una venta
ventas_router.add_api_route(
    path='/ventas/{id}',
    endpoint=ventas.delete,
    response_model=Venta,
    status_code=status.HTTP_200_OK,
    methods=['DELETE']
)