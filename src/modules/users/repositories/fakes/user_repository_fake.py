from typing import List
from src.modules.users.infra.models.user import User
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface


class UserRepositoryFake(UserRepositoryInterface):
    def __init__(self) -> None:
        self.users: List[User] = []

    def find_user_by_username(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        return None  # Return None if the user is not found
