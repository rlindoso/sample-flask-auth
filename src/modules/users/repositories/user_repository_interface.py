from abc import ABC, abstractmethod
from src.modules.users.infra.models.user import User

class UserRepositoryInterface(ABC):

    @abstractmethod
    def find_user_by_username(self, username: str) -> User:
        pass

