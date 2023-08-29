from fastapi import APIRouter
from api.pasos.routes import pasos_router
from api.ventas.routes import ventas_router
from api.entregas.routes import entregas_router
from api.clientes.routes import clientes_router
from api.tipo_productos.routes import tipo_productos_router
from api.usuarios.routes import usuarios_router
from api.productos.routes import productos_router


router = APIRouter(prefix='/api')
router.include_router(pasos_router, prefix="/pasos")
router.include_router(entregas_router, prefix="/entregas")
router.include_router(clientes_router, prefix="/clientes")
router.include_router(tipo_productos_router, prefix="/tipo_productos")
router.include_router(usuarios_router, prefix="/usuarios")
router.include_router(productos_router, prefix="/productos")
router.include_router(ventas_router, prefix="/ventas")