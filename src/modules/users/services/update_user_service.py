from models.user import User
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface
from src.shared.containers.providers.hash_providers.models.hash_provider_interface import HashProviderInterface
from src.shared.errors.error_types.http_bad_request import HttpBadRequestError


class UpdateUserService():
    def __init__(self, user_repository: UserRepositoryInterface, hash_provider: HashProviderInterface):
        self.user_repository = user_repository
        self.hash_provider = hash_provider

    def execute(self, user_id: int, password: str) -> User:
        if not user_id:
            raise HttpBadRequestError("It needs a user_id")
        
        if not password:
            raise HttpBadRequestError("It needs a password")
        
        user = self.user_repository.find_user_by_id(user_id=user_id)

        if not user:
            raise HttpBadRequestError("User does not exists")
        
        user.password = self.hash_provider.generate_hash(password)
        
        return self.user_repository.update_user(user=user)
        