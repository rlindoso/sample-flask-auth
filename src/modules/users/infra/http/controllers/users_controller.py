from flask import jsonify
from src.modules.users.infra.models.repositories.userRepository import UserRepository
from src.modules.users.services.create_user_service import CreateUserService
from src.modules.users.services.delete_user_service import DeleteUserService
from src.modules.users.services.show_user_by_username_service import ShowUserByUsernameService
from src.modules.users.services.update_user_service import UpdateUserService
from src.shared.containers.providers.hash_providers.implementations.bcrypt_hash_provider import BCryptHashProvider
from src.shared.infra.http.http_types.http_request import HttpRequest
from src.shared.infra.http.http_types.http_response import HttpResponse
from src.shared.infra.database.connection import db_connection_handler


class UsersController:
    def create(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.json.get("username")
        password = http_request.json.get("password")

        user_repository = UserRepository(db_connection_handler)
        hash_Provider = BCryptHashProvider()
        
        create_user_service = CreateUserService(user_repository=user_repository, hash_provider=hash_Provider)
        return jsonify(create_user_service.execute(username, password).to_dict()), 201
    
    def update(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.view_args["user_id"]
        password = http_request.json.get("password")

        user_repository = UserRepository(db_connection_handler)
        hash_Provider = BCryptHashProvider()
        
        update_user_service = UpdateUserService(user_repository=user_repository, hash_provider=hash_Provider)
        return jsonify(update_user_service.execute(user_id=user_id, password=password).to_dict()), 201
    
    def show(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.view_args["username"]

        user_repository = UserRepository(db_connection_handler)
        
        show_user_by_username_service = ShowUserByUsernameService(user_repository=user_repository)
        return jsonify(show_user_by_username_service.execute(username).to_dict()), 201
        
    def delete(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.view_args["user_id"]

        user_repository = UserRepository(db_connection_handler)
        
        delete_user_service = DeleteUserService(user_repository=user_repository)
        return jsonify(delete_user_service.execute(user_id=user_id).__dict__), 200
    