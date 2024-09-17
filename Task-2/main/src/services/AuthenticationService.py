from src.repositories.UserRepository import UserRepository
from src.entities.User import User

class AuthenticationService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def authenticate(self, username: str, password: str) -> User:
        for user in self.repository.users.values():
            if user.username == username and user.password == password:
                return user
        raise ValueError("Invalid username or password")

    def register_user(self, user: User):
        self.repository.add(user)
