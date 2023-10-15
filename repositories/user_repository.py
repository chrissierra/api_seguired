from uuid import UUID
from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.connection import get_db
from db.usuarios.models import UserDB


class UserRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def list(self) -> list[UserDB]:
        return self.db.query(UserDB).all()

    def create(self, nombre: str, email: str, rut: str, direccion: str):
        usuario = UserDB(nombre=nombre, email=email, rut=rut, direccion=direccion)
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario
    
    def update(self,  id: UUID, usuario: UserDB):
        print(f"El id es {id}")
        db_usuario = self.db.query(UserDB).filter(UserDB.id == id).first()
        if db_usuario is None:
            return None
        for var, value in vars(usuario).items():
            setattr(db_usuario, var, value)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    


    #def get_producto(self,  producto_id: int):
    def get_by_email(self, email: str) -> UserDB:
        print(email)
        # return self.db.query(Producto).filter(Producto.id == producto_id).first()
        return self.db.query(UserDB).filter(UserDB.email == email).first()
