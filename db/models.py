import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from db.connection import Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class UserDB(Base):
    __tablename__ = 'usuarios'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nombre = Column(String)
    rut = Column(String)
    direccion = Column(String)
    email = Column(String, unique=True)
    clientes = relationship("ClienteDB", back_populates="usuario", foreign_keys="[ClienteDB.usuario_id]")
    productos = relationship("ProductoDB", back_populates="usuario")


class PasoDB(Base):
    __tablename__ = 'pasos'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id_usuario = Column(UUID(as_uuid=True))
    tipo_producto_id = Column(UUID(as_uuid=True), ForeignKey('tipos_producto_a.id'))
    nombre_paso = Column(String)
    ordinalidad = Column(String)
    caracteristicas = Column(String)
    entregas = relationship('EntregaDB', secondary='pasos_entregas', back_populates='pasos')
    tipo_producto = relationship("TipoProductoDB", back_populates="pasos")

class PasoEntregaDB(Base):
    __tablename__ = 'pasos_entregas'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    paso_id = Column(UUID(as_uuid=True), ForeignKey('pasos.id'), nullable=False)
    entrega_id = Column(UUID(as_uuid=True), ForeignKey('entregas.id'), nullable=False)



class EntregaDB(Base):
    __tablename__ = 'entregas'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    ventas_id = Column(UUID(as_uuid=True), ForeignKey('ventas.id'))
    fecha = Column(String)
    pasos = relationship('PasoDB', secondary='pasos_entregas', back_populates='entregas')
    venta = relationship("VentaDB", back_populates="entregas", foreign_keys="[EntregaDB.ventas_id]")




class VentaDB(Base):
    __tablename__ = 'ventas'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    cliente_id = Column(UUID(as_uuid=True), ForeignKey('clientes.id'))
    entrega_id = Column(UUID(as_uuid=True), ForeignKey('entregas.id'), nullable=True)
    productos = relationship('ProductoDB', secondary='venta_producto', back_populates='ventas')
    cliente = relationship("ClienteDB", back_populates="ventas", foreign_keys=[cliente_id])
    entregas = relationship("EntregaDB", back_populates="venta", foreign_keys="[EntregaDB.ventas_id]")




class ClienteDB(Base):
    __tablename__ = 'clientes'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nombre = Column(String)
    direccion = Column(String)
    rut = Column(String)
    latitud = Column(Float)
    longitud = Column(Float)
    email = Column(String)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuarios.id'))
    ventas = relationship("VentaDB", back_populates="cliente", foreign_keys="[VentaDB.cliente_id]")
    usuario = relationship("UserDB", back_populates="clientes", foreign_keys="[ClienteDB.usuario_id]")





class TipoProductoDB(Base):
    __tablename__ = 'tipos_producto_a'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    usuario_id = Column(UUID(as_uuid=True))
    tipo_producto = Column(String)
    productos = relationship("ProductoDB", back_populates="tipo_producto", foreign_keys="[ProductoDB.tipo_producto_id]")
    pasos = relationship("PasoDB", back_populates="tipo_producto")






class ProductoDB(Base):
    __tablename__ = 'productos'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    tipo_producto_id = Column(UUID(as_uuid=True), ForeignKey('tipos_producto_a.id'))
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuarios.id'))  # Nueva columna
    nombre = Column(String)
    precio = Column(String)
    imagen = Column(String)
    tipo_producto = relationship("TipoProductoDB", back_populates="productos", foreign_keys="[ProductoDB.tipo_producto_id]")
    ventas = relationship('VentaDB', secondary='venta_producto', back_populates='productos')
    usuario = relationship("UserDB", back_populates="productos")  # Nuevo atributo de relación





class VentaProductoDB(Base):
    __tablename__ = 'venta_producto'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    venta_id = Column(UUID(as_uuid=True), ForeignKey('ventas.id'), nullable=False)
    producto_id = Column(UUID(as_uuid=True), ForeignKey('productos.id'), nullable=False)


