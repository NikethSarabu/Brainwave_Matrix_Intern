class User:
    def __init__(self, user_id: int, username: str, password: str, role: str):
        self.user_id = user_id
        self.username = username
        self.password = password  # Password field added
        self.role = role

    def change_password(self, new_password: str):
        """Change the user's password."""
        self.password = new_password

    def __str__(self):
        return f"User({self.user_id}, {self.username}, Role: {self.role})"
