from typing import Dict
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface
from src.shared.containers.providers.hash_providers.models.hash_provider_interface import HashProviderInterface
from src.shared.errors.error_types.http_bad_request import HttpBadRequestError


class AuthenticateUserService():
    def __init__(self, user_repository: UserRepositoryInterface, hash_provider: HashProviderInterface):
        self.user_repository = user_repository
        self.hash_provider = hash_provider
    
    def execute(self, username: str, password: str) -> Dict:
        if username and password:
            user = self.user_repository.find_user_by_username(username=username)

        if user and self.hash_provider.compare_hash(password, user.password):
            return user
        
        raise HttpBadRequestError("Invalid username or password")
