from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface
from src.shared.errors.error_types.http_bad_request import HttpBadRequestError

class IResponse:
    def __init__(self, message):
        self.message = message

class DeleteUserService():
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> IResponse:
        if not user_id:
            raise HttpBadRequestError("It needs a user_id")
        
        user = self.user_repository.find_user_by_id(user_id=user_id)

        if not user:
            raise HttpBadRequestError("User does not exists")
        
        self.user_repository.delete_user(user=user)

        return IResponse(message=f"User {user.username} deleted")
        