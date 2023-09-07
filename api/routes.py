from fastapi import APIRouter
from api.pasos.routes import pasos_router
from api.ventas.routes import ventas_router
from api.entregas.routes import entregas_router
from api.clientes.routes import clientes_router
from api.tipo_productos.routes import tipo_productos_router
from api.usuarios.routes import usuarios_router
from api.productos.routes import productos_router


router = APIRouter(prefix='/api')
router.include_router(pasos_router, )
router.include_router(entregas_router, )
router.include_router(clientes_router, )
router.include_router(tipo_productos_router, )
router.include_router(usuarios_router, )
router.include_router(productos_router, )
router.include_router(ventas_router, )