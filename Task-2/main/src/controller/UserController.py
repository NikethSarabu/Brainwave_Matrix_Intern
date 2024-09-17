from src.entities.User import User
from src.services.UserService import UserService

class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def add_user(self, user_id, username, password, role):
        try:
            user = User(user_id, username, password, role)
            self.user_service.add_user(user)
            return f"User {username} added successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def update_user(self,  user_id, username, password, role):
        try:
            user = User(user_id, username, password, role)
            self.user_service.update_user(user)
            return f"User {username} updated successfully."
        except ValueError as e:
            return f"Error: {str(e)}"

    def authenticate(self, username, password):
        try:
            user = self.user_service.authenticate(username, password)
            return user
        except ValueError as e:
            return f"Error: {str(e)}"
