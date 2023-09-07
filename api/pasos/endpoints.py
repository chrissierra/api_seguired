import uuid
from fastapi.params import Depends
from api.pasos.models import CreatePasos, PasosResponseModelListar, UpdatePasos
from repositories.pasos_repository import PasoRepository
from api.pasos.models import CreatePasoEstandar
from api.pasos.models import PasoEstandar
from api.pasos.models import Identificador

class PasosAPI:

    def list(self, pasos_repository: PasoRepository = Depends(PasoRepository)) -> list[PasosResponseModelListar]:
        return pasos_repository.get_pasos()

    def get(self, id: uuid.UUID, pasos_repository: PasoRepository = Depends(PasoRepository)) -> PasosResponseModelListar:
        return pasos_repository.get_paso(id)
    
    def get_pasos_estandar_by_id_usuario(self, id_usuario: uuid.UUID, pasos_repository: PasoRepository = Depends(PasoRepository)) -> PasosResponseModelListar:
        return pasos_repository.get_pasos_estandar_by_id_usuario(id_usuario)

    def create(self, paso: CreatePasos, entrega_id: Identificador, pasos_repository: PasoRepository = Depends(PasoRepository)) -> CreatePasos:
        return pasos_repository.create_paso(paso, entrega_id)
    
    def create_paso_estandar(self, paso_estandar: CreatePasoEstandar, pasos_repository: PasoRepository = Depends(PasoRepository)) -> PasoEstandar:
        return pasos_repository.create_paso_estandar(paso_estandar)

    def update(self, id: uuid.UUID, paso: UpdatePasos, pasos_repository: PasoRepository = Depends(PasoRepository)) -> PasosResponseModelListar:
        return pasos_repository.update_paso(id, paso)

    def delete(self, id: uuid.UUID, pasos_repository: PasoRepository = Depends(PasoRepository)):
        return pasos_repository.delete_paso(id)