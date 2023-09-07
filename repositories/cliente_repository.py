from uuid import UUID
from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from db.clientes.models import ClienteDB


# from .models import ClienteDB  # Asegúrate de que la ruta sea correcta

class ClienteRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get_clientes(self, skip: int = 0, limit: int = 10):
        return self.db.query(ClienteDB).offset(skip).limit(limit).all()
    
    def get_clientes_by_id_usuario(self, id: UUID, skip: int = 0, limit: int = 10):
        print(id)
        return self.db.query(ClienteDB).filter(ClienteDB.usuario_id == id).offset(skip).limit(limit).all()

    
    def get_cliente(self, cliente_id: int):
        return self.db.query(ClienteDB).filter(ClienteDB.id == cliente_id).first()

    
    def create_cliente(self, nombre, direccion, rut, latitud, longitud, usuario_id, email):
        cliente = ClienteDB(
            nombre=nombre, 
            direccion=direccion,
            rut=rut,
            latitud=latitud,
            longitud=longitud,
            usuario_id=usuario_id,
            email=email
        )
        self.db.add(cliente)
        self.db.commit()
        self.db.refresh(cliente)
        return cliente

    
    def update_cliente(self, id_cliente: UUID, cliente: ClienteDB):
        db_cliente = self.db.query(ClienteDB).filter(ClienteDB.id == id_cliente).first()
        if db_cliente is None:
            return None
        for var, value in vars(cliente).items():
            setattr(db_cliente, var, value)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente

    
    def delete_cliente(db: Session, cliente_id: int):
        db_cliente = db.query(ClienteDB).filter(ClienteDB.id == cliente_id).first()
        if db_cliente is None:
            return None
        db.delete(db_cliente)
        db.commit()
        return db_cliente