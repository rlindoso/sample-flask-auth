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
        return jsonify(authenticate_user_service.execute(username, password)), 201
    