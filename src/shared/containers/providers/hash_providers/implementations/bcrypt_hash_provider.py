from bcrypt import checkpw, gensalt, hashpw
from src.shared.containers.providers.hash_providers.models.hash_provider_interface import HashProviderInterface


class BCryptHashProvider(HashProviderInterface):
    def generate_hash(self, payload: str) -> str:
        hashed_payload = hashpw(payload.encode('utf8'), gensalt())
        return hashed_payload.decode('utf8')

    def compare_hash(self, payload: str, hashed: str) -> bool:
        return checkpw(str.encode(payload), str.encode(hashed))
