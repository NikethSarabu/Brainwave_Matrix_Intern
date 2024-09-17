from src.repositories.UserRepository import UserRepository
from src.entities.User import User

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

    def authenticate(self, username, password):
        user = self.repository.find_by_username(username)
        if user and user.password == password:
            return user
        else:
            raise ValueError("Invalid username or password")

    def list_all_users(self):
        return self.repository.get_all_users()

    def change_password(self, username, old_password, new_password):
        user = self.repository.get_by_username(username)
        if user and user.password == old_password:
            user.password = new_password
        else:
            raise ValueError("Invalid old password")