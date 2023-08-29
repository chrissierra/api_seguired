import uuid
from fastapi.params import Depends
from api.usuarios.models import CreateUser, User
from repositories.user_repository import UserRepository

class UserAPI:

    def list(self, student_repository: UserRepository = Depends(UserRepository)) -> list[User]:
        return student_repository.list()

    def create(self, usuario: CreateUser, user_repository: UserRepository = Depends(UserRepository)) -> User:
        return user_repository.create(nombre=usuario.nombre, email=usuario.email, direccion=usuario.direccion, rut=usuario.rut)
    
    def get(self, email: str, user_repository: UserRepository = Depends(UserRepository)) -> User:
        return user_repository.get_by_email(email)
