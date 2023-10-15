from fastapi import Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from sqlalchemy.orm import joinedload
from api.ventas.models import CreateVenta, UpdateVenta
from db.ventas.models import VentaDB
from db.productos.models import ProductoDB
from db.venta_producto.models import VentaProductoDB
from api.ventas.models import CantidadesPorVenta
from db.ventas.models import ProductoVentaCantidadDB
from db.entregas.models import EntregaDB
from api.ventas.models import Fecha
class VentaRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_ventas(self):
        return self.db.query(VentaDB).all()

    def get_venta(self, id: int):
        response = self.db.query(VentaDB).options(
            joinedload(VentaDB.productos),
            joinedload(VentaDB.cliente),
            joinedload(VentaDB.entregas),
            joinedload(VentaDB.usuario)
        ).filter(VentaDB.id == id).first()
        for field, value in vars(response).items():
            if not field.startswith("_"):
                print(f"{field}: {value}")
        return response
    
    def get_venta_by_id_usuario(self, id_usuario: int):
        response = self.db.query(VentaDB).options(
            joinedload(VentaDB.productos),
            joinedload(VentaDB.cliente),
            joinedload(VentaDB.entregas).joinedload(EntregaDB.pasos)
        ).filter(VentaDB.usuario_id == id_usuario).all()
        print(response)
        return response

    def create_venta(self, venta: CreateVenta, producto_ids: list, lista_cantidades: list[CantidadesPorVenta], entrega: Fecha):        
        db_venta = VentaDB(**venta.dict())
        self.db.add(db_venta)
        self.db.commit()
        self.db.refresh(db_venta)

        # Obtén los productos a partir de sus IDs
        productos = self.db.query(ProductoDB).filter(ProductoDB.id.in_(producto_ids)).all()

        # Asocia los productos con la venta en la tabla venta_producto
        for producto in productos:
            nueva_asociacion = VentaProductoDB(venta_id=db_venta.id, producto_id=producto.id)
            self.db.add(nueva_asociacion)

        for item in lista_cantidades:
            nueva_cantidad = ProductoVentaCantidadDB(
                cantidad=item.cantidad,
                subtotal=item.subtotal,
                venta_id=db_venta.id,
                producto_id=item.producto_id
            )
            self.db.add(nueva_cantidad)

        db_entrega = EntregaDB(ventas_id=db_venta.id, fecha=entrega.fecha)
        self.db.add(db_entrega)
        self.db.commit()
        db_venta.entrega_id = db_entrega.id
        self.db.commit()

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