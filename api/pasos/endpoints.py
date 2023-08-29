import uuid
from fastapi.params import Depends
from api.pasos.models import CreatePasos, PasosResponseModelListar, UpdatePasos
from repositories.pasos_repository import PasoRepository

class PasosAPI:

    def list(self, pasos_repository: PasoRepository = Depends(PasoRepository)) -> list[PasosResponseModelListar]:
        return pasos_repository.get_pasos()

    def get(self, id: uuid.UUID, pasos_repository: PasoRepository = Depends(PasoRepository)) -> PasosResponseModelListar:
        return pasos_repository.get_paso(id)

    def create(self, paso: CreatePasos, pasos_repository: PasoRepository = Depends(PasoRepository)) -> CreatePasos:
        return pasos_repository.create_paso(paso)

    def update(self, id: uuid.UUID, paso: UpdatePasos, pasos_repository: PasoRepository = Depends(PasoRepository)) -> PasosResponseModelListar:
        return pasos_repository.update_paso(id, paso)

    def delete(self, id: uuid.UUID, pasos_repository: PasoRepository = Depends(PasoRepository)):
        return pasos_repository.delete_paso(id)