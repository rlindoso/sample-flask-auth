from pytest import raises
from src.modules.users.infra.models.user import User
from src.modules.users.repositories.fakes.user_repository_fake import UserRepositoryFake
from src.modules.users.services.authenticate_user_service import AuthenticateUserService
from src.shared.containers.providers.hash_providers.fakes.fake_hash_provider import FakeHashProvider


def test_login():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()
    user = User()
    user.username = "test"
    user.password = hash_provider.generate_hash("123456")
    user_repository.users.append(user)

    authenticate_user_service = AuthenticateUserService(user_repository=user_repository, hash_provider=hash_provider)
    result = authenticate_user_service.execute(user.username, "123456")
    assert result == {'message': 'Logged in'}

def test_failure():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()
    user = User()
    user.username = "test"
    user.password = hash_provider.generate_hash("123456")
    user_repository.users.append(user)

    authenticate_user_service = AuthenticateUserService(user_repository=user_repository, hash_provider=hash_provider)
    with raises(Exception) as excinfo:
        authenticate_user_service.execute(user.username, "wrong password")

    assert str(excinfo.value) == "Invalid username or password"