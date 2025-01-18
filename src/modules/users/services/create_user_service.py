from src.modules.users.infra.models.user import User
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface
from src.shared.containers.providers.hash_providers.models.hash_provider_interface import HashProviderInterface
from src.shared.errors.error_types.http_bad_request import HttpBadRequestError


class CreateUserService():
    def __init__(self, user_repository: UserRepositoryInterface, hash_provider: HashProviderInterface):
        self.user_repository = user_repository
        self.hash_provider = hash_provider

    def execute(self, username: str, password: str) -> User:
        if username and password:
            hashed_password = self.hash_provider.generate_hash(password)
            user = self.user_repository.create_user(User(username=username, password=hashed_password))

            return user
        
        raise HttpBadRequestError("It needs a username and password")