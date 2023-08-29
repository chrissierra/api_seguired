from typing import List
import uuid
from fastapi.params import Depends
from api.clientes.models import Cliente, CreateCliente, UpdateCliente
from repositories.cliente_repository import ClienteRepository

class ClienteAPI:

    def list(self, cliente_repository: ClienteRepository = Depends(ClienteRepository)) -> list[Cliente]:
        return cliente_repository.get_clientes()
    
    def list_by_id_usuario(self, id: uuid.UUID, cliente_repository: ClienteRepository = Depends(ClienteRepository)) -> List[Cliente]:
        return cliente_repository.get_clientes_by_id_usuario(id)

    def get(self, id: uuid.UUID, cliente_repository: ClienteRepository = Depends(ClienteRepository)) -> Cliente:
        return cliente_repository.get_cliente(id)

    def create(self, cliente: CreateCliente, cliente_repository: ClienteRepository = Depends(ClienteRepository)) -> Cliente:
        return cliente_repository.create_cliente(cliente.nombre,\
        cliente.direccion,\
        cliente.rut,\
        cliente.latitud,\
        cliente.longitud,\
        cliente.usuario_id,\
        cliente.email)

    def update(self, id: uuid.UUID, cliente: UpdateCliente, cliente_repository: ClienteRepository = Depends(ClienteRepository)) -> Cliente:
        return cliente_repository.update_cliente(id, cliente)

    def delete(self, id: uuid.UUID, cliente_repository: ClienteRepository = Depends(ClienteRepository)):
        return cliente_repository.delete_cliente(id)