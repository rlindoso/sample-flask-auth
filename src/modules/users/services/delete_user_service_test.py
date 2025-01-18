from pytest import raises
from src.modules.users.infra.models.user import User
from src.modules.users.repositories.fakes.user_repository_fake import UserRepositoryFake
from src.modules.users.services.delete_user_service import DeleteUserService


def test_delete_user():
    user_repository = UserRepositoryFake()
    user = User(id=1, username="test", password="123456")
    user_repository.users.append(user)
    
    update_user_service = DeleteUserService(user_repository=user_repository)
    result = update_user_service.execute(user_id=user.id)

    assert result.__dict__ == {"message": f"User {user.username} deleted"}
    assert result.message == f"User {user.username} deleted"
    deletedUser = user_repository.find_user_by_id(user_id=user.id)
    assert deletedUser ==  None

def test_error_if_not_has_user_id():
    user_repository = UserRepositoryFake()
    user = User(id=1, username="test", password="123456")
    user_repository.users.append(user)
    
    update_user_service = DeleteUserService(user_repository=user_repository)

    with raises(Exception) as excinfo:
        update_user_service.execute(user_id=None)
    
    assert str(excinfo.value) == "It needs a user_id"


def test_error_if_user_does_not_exists():
    user_repository = UserRepositoryFake()
    user = User(id=1, username="test", password="123456")
    user_repository.users.append(user)
    
    update_user_service = DeleteUserService(user_repository=user_repository)

    with raises(Exception) as excinfo:
        update_user_service.execute(user_id=123)
    
    assert str(excinfo.value) == "User does not exists"
