from repositories.UserRepository import UserRepository
from entities.User import User

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def add_user(self, user: User):
        self.repository.add(user)

    def get_user(self, user_id: int) -> User:
        return self.repository.get(user_id)

    def delete_user(self, user_id: int):
        self.repository.delete(user_id)

    def update_user(self, user: User):
        self.repository.update(user)
