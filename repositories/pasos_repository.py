from typing import Optional
from uuid import UUID
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.connection import get_db
from db.pasos.models import PasoDB
from api.pasos.models import CreatePasoEstandar
from db.pasos.models import PasosEstandarDB
from db.paso_entrega.models import PasoEntregaDB
from api.pasos.models import Identificador

class PasosModel(BaseModel):
    id: UUID
    id_usuario: UUID
    tipo_producto_id: Optional[UUID] = None
    id_paso_estandar: UUID
    """ nombre_paso: str """
    caracteristicas: str
    ordinalidad: str
    class Config:
        orm_mode = True

class PasoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get_pasos(self, skip: int = 0, limit: int = 10):
        return self.db.query(PasoDB).offset(skip).limit(limit).all()

    
    def get_paso(self, paso_id: UUID):
        print('Buscando PASO')
        return self.db.query(PasoDB).filter(PasoDB.id == paso_id).first()
    
    def get_pasos_estandar_by_id_usuario(self, usuario_id: UUID):
        return self.db.query(PasosEstandarDB).filter(PasosEstandarDB.id_usuario == usuario_id).all()

    
    def create_paso(self, paso: PasosModel, entrega_id: Identificador):
        pasos = PasoDB(**paso.dict())
        self.db.add(pasos)
        print(entrega_id)
        self.db.commit()
        paso_entrega = PasoEntregaDB(paso_id = pasos.id, entrega_id = entrega_id.id)
        self.db.add(paso_entrega)
        self.db.commit()

        self.db.refresh(pasos)
        return paso

    def create_paso_estandar(self, paso_estandar: CreatePasoEstandar):
        pasos = PasosEstandarDB(**paso_estandar.dict())
        self.db.add(pasos)
        self.db.commit()
        self.db.refresh(pasos)
        print(pasos)
        return pasos.__dict__

    
    def update_paso(self, id: UUID ,paso: PasoDB):
        db_paso = self.db.query(PasoDB).filter(PasoDB.id == id).first()
        if db_paso is None:
            return None
        for var, value in vars(paso).items():
            setattr(db_paso, var, value)
        self.db.commit()
        self.db.refresh(db_paso)
        return db_paso

    
    def delete_paso(self, paso_id: int):
        db_paso = self.db.query(PasoDB).filter(PasoDB.id == paso_id).first()
        if db_paso is None:
            return None
        self.db.delete(db_paso)
        self.db.commit()
        return db_paso