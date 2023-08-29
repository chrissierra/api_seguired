from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from uuid import UUID
from sqlalchemy.orm import joinedload

from db.models import ProductoDB
# from .models import Productos  # Asegúrate de que la ruta sea correcta

class ProductoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get_productos(self,  skip: int = 0, limit: int = 10):
        return self.db.query(ProductoDB).offset(skip).limit(limit).all()

    
    def get_producto(self,  producto_id: int):
        return self.db.query(ProductoDB).filter(ProductoDB.id == producto_id).first()
    
    def get_producto_by_user_id(self,  usuario_id: int):
        return self.db.query(ProductoDB)\
        .options(
                joinedload(ProductoDB.tipo_producto),
                joinedload(ProductoDB.usuario)
            ).filter(ProductoDB.usuario_id == usuario_id).all()

    
    def create_producto(self, tipo_producto_id: UUID,nombre:str, precio:str, imagen:str, usuario_id: UUID):
        producto = ProductoDB(
            tipo_producto_id=tipo_producto_id,
            nombre=nombre,
            precio=precio,
            imagen=imagen,
            usuario_id=usuario_id
        )
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    
    def update_producto(self,  id: UUID, producto: ProductoDB):
        db_producto = self.db.query(ProductoDB).filter(ProductoDB.id == id).first()
        if db_producto is None:
            return None
        for var, value in vars(producto).items():
            setattr(db_producto, var, value)
        self.db.commit()
        self.db.refresh(db_producto)
        return db_producto

    
    def delete_producto(self,  producto_id: int):
        db_producto = self.db.query(ProductoDB).filter(ProductoDB.id == producto_id).first()
        if db_producto is None:
            return None
        self.db.delete(db_producto)
        self.db.commit()
        return db_producto