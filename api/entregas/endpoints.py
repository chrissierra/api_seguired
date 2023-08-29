import uuid
from fastapi.params import Depends
from api.entregas.models import CreateEntrega, EntregaModel, EntregaModelListar, UpdateEntrega
from repositories.entrega_repository import EntregaRepository

class EntregaAPI:

    def list(self, entrega_repository: EntregaRepository = Depends(EntregaRepository)) -> list[EntregaModelListar]:
        return entrega_repository.get_entregas()

    def get(self, id: uuid.UUID, entrega_repository: EntregaRepository = Depends(EntregaRepository)) -> EntregaModel:
        return entrega_repository.get_entrega(id)

    def create(self, entrega: CreateEntrega, entrega_repository: EntregaRepository = Depends(EntregaRepository)) -> EntregaModel:
        return entrega_repository.create_entrega(entrega)

    def update(self, id: uuid.UUID, entrega: UpdateEntrega, entrega_repository: EntregaRepository = Depends(EntregaRepository)) -> EntregaModel:
        return entrega_repository.update_entrega(id, entrega)

    def delete(self, id: uuid.UUID, entrega_repository: EntregaRepository = Depends(EntregaRepository)):
        return entrega_repository.delete_entrega(id)