from src.modules.users.infra.models.user import User
from sqlalchemy.orm.exc import NoResultFound
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface
from src.shared.infra.database.connection import DBConnectionHandler


class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
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

    def create_user(self, user: User) -> User:
        username = user.username
        password = user.password
        with self.__db_connection as database:
            try:
                user
                database.session.add(user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
        return User(username=username, password=password)
            
    def update_user(self, user: User) -> User:
        with self.__db_connection as database:
            try:
                user
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_user(self, user_id: int) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .get(user_id)
                        .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception