from src.modules.users.infra.models.user import User
from src.modules.users.repositories.fakes.user_repository_fake import UserRepositoryFake
from src.modules.users.services.authenticate_user_service import AuthenticateUserService


def test_login():
    userRepository = UserRepositoryFake()
    user = User()
    user.username = "test"
    user.password = "123456"
    userRepository.users.append(user)

    authenticate_user_service = AuthenticateUserService(userRepository)
    result = authenticate_user_service.execute(user.username, user.password)
    assert result == {'message': 'Logged in'}

def test_failure():
    userRepository = UserRepositoryFake()
    user = User()
    user.username = "test"
    user.password = "123456"
    userRepository.users.append(user)

    authenticate_user_service = AuthenticateUserService(userRepository)
    result = authenticate_user_service.execute(user.username, "wrong password")
    assert result == {'message': 'Invalid username or password'}