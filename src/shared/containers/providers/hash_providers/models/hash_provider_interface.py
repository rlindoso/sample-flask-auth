from abc import ABC, abstractmethod
from src.modules.users.infra.models.user import User

class HashProviderInterface(ABC):

    @abstractmethod
    def generate_hash(self, payload: str) -> str:
        pass

    @abstractmethod
    def compare_hash(self, payload: str, hashed: str) -> bool:
        pass

