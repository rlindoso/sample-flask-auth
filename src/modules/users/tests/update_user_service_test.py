from pytest import raises
from src.modules.users.infra.models.user import User
from src.modules.users.repositories.fakes.user_repository_fake import UserRepositoryFake
from src.modules.users.services.update_user_service import UpdateUserService
from src.shared.containers.providers.hash_providers.fakes.fake_hash_provider import FakeHashProvider


def test_update_user():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()
    user = User(id=1, username="test", password=hash_provider.generate_hash("123456"))
    user_repository.users.append(user)
    
    update_user_service = UpdateUserService(user_repository=user_repository, hash_provider=hash_provider)
    user = update_user_service.execute(user_id=user.id, password="new password")

    assert user.id == 1
    assert user.password ==  hash_provider.generate_hash("new password")

def test_error_if_not_has_user_id():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()
    user = User(id=1, username="test", password=hash_provider.generate_hash("123456"))
    user_repository.users.append(user)
    
    update_user_service = UpdateUserService(user_repository=user_repository, hash_provider=hash_provider)

    with raises(Exception) as excinfo:
        update_user_service.execute(user_id=None, password="123456")
    
    assert str(excinfo.value) == "It needs a user_id"

def test_error_if_not_has_password():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()
    user = User(id=1, username="test", password=hash_provider.generate_hash("123456"))
    user_repository.users.append(user)
    
    update_user_service = UpdateUserService(user_repository=user_repository, hash_provider=hash_provider)

    with raises(Exception) as excinfo:
        update_user_service.execute(user_id=user.id, password=None)
    
    assert str(excinfo.value) == "It needs a password"

def test_error_if_user_does_not_exists():
    user_repository = UserRepositoryFake()
    hash_provider = FakeHashProvider()
    user = User(id=1, username="test", password=hash_provider.generate_hash("123456"))
    user_repository.users.append(user)
    
    update_user_service = UpdateUserService(user_repository=user_repository, hash_provider=hash_provider)

    with raises(Exception) as excinfo:
        update_user_service.execute(user_id=123, password="22333")
    
    assert str(excinfo.value) == "User does not exists"
