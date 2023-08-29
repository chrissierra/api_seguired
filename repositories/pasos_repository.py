from uuid import UUID
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.connection import get_db
from db.models import PasoDB


class PasosModel(BaseModel):
    id: UUID
    id_usuario: UUID
    tipo_producto_id: UUID
    nombre_paso: str
    caracteristicas: str
    ordinalidad: str

class PasoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get_pasos(self, skip: int = 0, limit: int = 10):
        return self.db.query(PasoDB).offset(skip).limit(limit).all()

    
    def get_paso(self, paso_id: UUID):
        print('Buscando PASO')
        return self.db.query(PasoDB).filter(PasoDB.id == paso_id).first()

    
    def create_paso(self, paso: PasosModel):
        pasos = PasoDB(**paso.dict())
        self.db.add(pasos)
        self.db.commit()
        self.db.refresh(pasos)
        return paso
        # return PasosModel(**atributos_configurados)

    
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