from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.connection import get_db
from db.models import UserDB


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
    
    #def get_producto(self,  producto_id: int):
    def get_by_email(self, email: str) -> UserDB:
        print(email)
        # return self.db.query(Producto).filter(Producto.id == producto_id).first()
        return self.db.query(UserDB).filter(UserDB.email == email).first()
