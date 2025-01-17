from typing import List
from src.modules.users.infra.models.user import User
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface


class UserRepositoryFake(UserRepositoryInterface):
    def __init__(self) -> None:
        self.users: List[User] = []
        self.id = 0

    def find_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None  # Return None if the user is not found

    def find_user_by_username(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        return None  # Return None if the user is not found

    def create_user(self, user: User) -> User:
        self.id += 1
        user.id = self.id
        self.users.append(user)
        return user
            
    def update_user(self, user: User) -> User:
        for repo_user in self.users:
            if repo_user.id == user.id:
                repo_user = user
                return repo_user
        return None

    def delete_user(self, user_id: int) -> None:
        self.users = [user for user in self.users if user.id != user_id]