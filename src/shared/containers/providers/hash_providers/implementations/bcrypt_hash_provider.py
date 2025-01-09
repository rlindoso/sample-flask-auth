from bcrypt import checkpw, gensalt, hashpw
from src.shared.containers.providers.hash_providers.models.hash_provider_interface import HashProviderInterface


class BCryptHashProvider(HashProviderInterface):
    def generate_hash(self, payload: str) -> str:
        return hashpw(payload.encode('utf8'), gensalt())

    def compare_hash(self, payload: str, hashed: str) -> bool:
        passwd = payload.decode('utf8')
        return checkpw(payload, hashed)
