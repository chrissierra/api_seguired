from uuid import UUID
from sqlalchemy.orm import Session
from db.connection import get_db
from fastapi.params import Depends

from api.entregas.models import EntregaModel
from db.entregas.models import EntregaDB
# from .models import EntregaDB  # Asegúrate de que la ruta sea correcta

class EntregaRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get_entregas(self, skip: int = 0, limit: int = 10):
        return self.db.query(EntregaDB).offset(skip).limit(limit).all()

    
    def get_entrega(self, entrega_id: UUID):
        return self.db.query(EntregaDB).filter(EntregaDB.id == entrega_id).first()

    
    def create_entrega(self, entrega: EntregaModel):
        instanciaEntrega = EntregaDB(**entrega.dict())
        self.db.add(instanciaEntrega)
        self.db.commit()
        self.db.refresh(instanciaEntrega)
        return instanciaEntrega

    
    def update_entrega(self, entrega: EntregaDB):
        db_entrega = self.db.query(EntregaDB).filter(EntregaDB.id == entrega.id).first()
        if db_entrega is None:
            return None
        for var, value in vars(entrega).items():
            setattr(db_entrega, var, value)
        self.db.commit()
        self.db.refresh(db_entrega)
        return db_entrega

    
    def delete_entrega(self, entrega_id: int):
        db_entrega = self.db.query(EntregaDB).filter(EntregaDB.id == entrega_id).first()
        if db_entrega is None:
            return None
        self.db.delete(db_entrega)
        self.db.commit()
        return db_entrega