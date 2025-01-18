from flask_login import login_user
from models.user import User
from src.modules.users.infra.models.repositories.userRepository import UserRepository
from src.modules.users.services.authenticate_user_service import AuthenticateUserService
from src.shared.containers.providers.hash_providers.implementations.bcrypt_hash_provider import BCryptHashProvider
from src.shared.infra.http.http_types.http_request import HttpRequest
from src.shared.infra.http.http_types.http_response import HttpResponse
from src.shared.infra.database.connection import db_connection_handler
from flask import jsonify


class SessionsController:
    def create(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.json.get("username")
        password = http_request.json.get("password")

        user_repository = UserRepository(db_connection_handler)
        hash_Provider = BCryptHashProvider()
        
        authenticate_user_service = AuthenticateUserService(user_repository=user_repository, hash_provider=hash_Provider)
        login_user(authenticate_user_service.execute(username, password))
        return jsonify({"message": "Logged in"}), 201
    
    def get_user(self, user_id) -> User:
        user_repository = UserRepository(db_connection_handler)
        return user_repository.find_user_by_id(user_id=user_id)