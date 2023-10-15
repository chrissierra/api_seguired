from fastapi import APIRouter
from starlette import status

from api.usuarios.endpoints import UserAPI
from api.usuarios.models import User



usuarios = UserAPI()
usuarios_router =  APIRouter()
usuarios_router.add_api_route(path='/usuarios', endpoint=usuarios.list, response_model=list[User], status_code=status.HTTP_200_OK, methods=['GET'])
usuarios_router.add_api_route(path='/usuarios', endpoint=usuarios.create, response_model=User, status_code=status.HTTP_201_CREATED, methods=['POST'])
usuarios_router.add_api_route(path='/usuario', endpoint=usuarios.get, response_model=User, status_code=status.HTTP_200_OK, methods=['GET'])

usuarios_router.add_api_route(path='/usuario/{id}', endpoint=usuarios.update, response_model=User, status_code=status.HTTP_200_OK, methods=['PUT'])
