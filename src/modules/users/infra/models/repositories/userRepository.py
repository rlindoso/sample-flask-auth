from src.modules.users.infra.models.user import User
from sqlalchemy.orm.exc import NoResultFound
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def find_user_by_username(self, username: str) -> User:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                        .query(User)
                        .filter(User.username == username)
                        .one()
                )
                return person
            except NoResultFound:
                return None
