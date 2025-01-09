from pytest import raises
from src.modules.users.repositories.fakes.user_repository_fake import UserRepositoryFake
from src.modules.users.services.create_user_service import CreateUserService
from src.shared.containers.providers.hash_providers.fakes.fake_hash_provider import FakeHashProvider


def test_create_user():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()

    username = "user_test"
    password = "123456"

    create_user_service = CreateUserService(user_repository=user_repository, hash_provider=hash_provider)
    user = create_user_service.execute(username, password)

    assert user.id == 1
    assert user.username == "user_test"
    assert user.password ==  hash_provider.generate_hash("123456")

def test_error_if_not_has_username():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()

    username = ""
    password = "123456"

    create_user_service = CreateUserService(user_repository=user_repository, hash_provider=hash_provider)

    with raises(Exception) as excinfo:
        create_user_service.execute(username, password)
    
    assert str(excinfo.value) == "It needs a username and password"

def test_error_if_not_has_password():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()

    username = "user_test"
    password = ""

    create_user_service = CreateUserService(user_repository=user_repository, hash_provider=hash_provider)

    with raises(Exception) as excinfo:
        create_user_service.execute(username, password)
    
    assert str(excinfo.value) == "It needs a username and password"