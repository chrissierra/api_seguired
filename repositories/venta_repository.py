from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from sqlalchemy.orm import joinedload
from api.ventas.models import CreateVenta, UpdateVenta
from db.models import VentaDB

class VentaRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_ventas(self):
        return self.db.query(VentaDB).all()

    def get_venta(self, id: int):
        response = self.db.query(VentaDB).options(
            joinedload(VentaDB.productos),
            joinedload(VentaDB.cliente),
            joinedload(VentaDB.entregas)
        ).filter(VentaDB.id == id).first()
        for field, value in vars(response).items():
            if not field.startswith("_"):
                print(f"{field}: {value}")
        return response
        #return self.db.query(Venta).filter(Venta.id == id).first()

    def create_venta(self, venta: CreateVenta):        
        db_venta = VentaDB(**venta.dict())
        self.db.add(db_venta)
        self.db.commit()
        self.db.refresh(db_venta)
        return db_venta

    def update_venta(self, id: int, venta: UpdateVenta):
        db_venta = self.db.query(VentaDB).filter(VentaDB.id == id).first()
        if db_venta is None:
            return None
        for key, value in venta.dict().items():
            setattr(db_venta, key, value)
        self.db.commit()
        self.db.refresh(db_venta)
        return db_venta

    def delete_venta(self, id: int):
        db_venta = self.db.query(VentaDB).filter(VentaDB.id == id).first()
        if db_venta is None:
            return None
        self.db.delete(db_venta)
        self.db.commit()
        return db_venta