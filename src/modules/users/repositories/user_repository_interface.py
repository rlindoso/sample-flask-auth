from abc import ABC, abstractmethod
from src.modules.users.infra.models.user import User

class UserRepositoryInterface(ABC):

    @abstractmethod
    def find_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def find_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass