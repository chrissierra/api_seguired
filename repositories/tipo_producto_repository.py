from fastapi.params  import Depends
from sqlalchemy.orm import Session

from db.connection import get_db
from uuid import UUID

from db.models import TipoProductoDB

class TipoProductoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def get_tipos_producto(self,  skip: int = 0, limit: int = 10):
        return self.db.query(TipoProductoDB).offset(skip).limit(limit).all()

    
    def get_tipo_producto(self,  tipo_producto_id: int):
        return self.db.query(TipoProductoDB).filter(TipoProductoDB.id == tipo_producto_id).first()
    
    def get_by_id_usuario(self,  usuario_id: int):
        return self.db.query(TipoProductoDB).filter(TipoProductoDB.usuario_id == usuario_id).all()

    
    def create_tipo_producto(self,  usuario_id: UUID, tipo_producto: str ):
        db_tipo_producto = TipoProductoDB(
            usuario_id=usuario_id,
            tipo_producto=tipo_producto,
        )
        self.db.add(db_tipo_producto)
        self.db.commit()
        self.db.refresh(db_tipo_producto)
        return db_tipo_producto

    
    def update_tipo_producto(self,  tipo_producto: TipoProductoDB):
        db_tipo_producto = self.db.query(TipoProductoDB).filter(TipoProductoDB.id == tipo_producto.id).first()
        if db_tipo_producto is None:
            return None
        for var, value in vars(tipo_producto).items():
            setattr(db_tipo_producto, var, value)
        self.db.commit()
        self.db.refresh(db_tipo_producto)
        return db_tipo_producto

    
    def delete_tipo_producto(self,  tipo_producto_id: int):
        db_tipo_producto = self.db.query(TipoProductoDB).filter(TipoProductoDB.id == tipo_producto_id).first()
        if db_tipo_producto is None:
            return None
        self.db.delete(db_tipo_producto)
        self.db.commit()
        return db_tipo_producto