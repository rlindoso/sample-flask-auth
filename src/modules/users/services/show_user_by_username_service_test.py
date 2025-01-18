from pytest import raises
from src.modules.users.infra.models.user import User
from src.modules.users.repositories.fakes.user_repository_fake import UserRepositoryFake
from src.modules.users.services.show_user_by_username_service import ShowUserByUsernameService


def test_get_user():
    user_repository = UserRepositoryFake()
    user = User(id=123, username="test", password="123456")
    user_repository.users.append(user)

    show_user_by_username_service = ShowUserByUsernameService(user_repository=user_repository)
    result = show_user_by_username_service.execute(user.username)
    assert user.id == result.id

def test_user_does_not_exists():
    user_repository = UserRepositoryFake()
    user = User(id=123, username="test", password="123456")
    user_repository.users.append(user)

    show_user_by_username_service = ShowUserByUsernameService(user_repository=user_repository)
    with raises(Exception) as excinfo:
        show_user_by_username_service.execute("does not exists")

    assert str(excinfo.value) == "User does not exists"
