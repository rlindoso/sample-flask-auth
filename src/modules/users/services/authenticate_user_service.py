from bcrypt import checkpw
from flask import jsonify
from flask_login import login_user
from src.modules.users.repositories.user_repository_interface import UserRepositoryInterface

class RequestInterface:
    username: str
    password: str


class AuthenticateUserService():
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
    
    def execute(self, username: str, password: str):
        if username and password:
            user = self.user_repository.find_user_by_username(username=username)
            passwd = str.encode(password)
            usr_passwd = str.encode(user.password)

        # if user and checkpw(passwd, usr_passwd):
        if user and passwd == usr_passwd:
            # login_user(user)
            return {"message": "Logged in"}
    
        return {"message": "Invalid username or password"}
