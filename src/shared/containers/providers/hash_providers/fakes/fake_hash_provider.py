from src.shared.containers.providers.hash_providers.models.hash_provider_interface import HashProviderInterface


class FakeHashProvider(HashProviderInterface):
    def generate_hash(self, payload: str) -> str:
        return f"payload_hashed_{payload}"

    def compare_hash(self, payload: str, hashed: str) -> bool:
        return (f"payload_hashed_{payload}" == hashed)
