from typing import Dict
from src.entities.User import User

class UserRepository:
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add(self, user: User):
        self.users[user.user_id] = user

    def get(self, user_id: int) -> User:
        return self.users.get(user_id)

    def delete(self, user_id: int):
        if user_id in self.users:
            del self.users[user_id]

    def update(self, user: User):
        self.users[user.user_id] = user

    def find_by_username(self, username):
        for user in self.users.values():
            if user.username == username:
                return user
        return None