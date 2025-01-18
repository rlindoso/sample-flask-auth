from src.modules.users.infra.models.user import User
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface
from src.shared.errors.error_types.http_bad_request import HttpBadRequestError


class ShowUserByUsernameService():
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, username: str) -> User:
        user = self.user_repository.find_user_by_username(username=username)

        if not user:
            raise HttpBadRequestError("User does not exists")
        
        return user
        
