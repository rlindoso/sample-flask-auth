from flask import Blueprint, request
from src.modules.users.infra.http.controllers.sessions_controller import SessionsController
from src.modules.users.infra.http.controllers.users_controller import UsersController

user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route('/login', methods=["POST"])
def login():
    sessions_controller = SessionsController()
    return sessions_controller.create(request)

@user_route_bp.route('/user', methods=["POST"])
def create_user():
    users_controller = UsersController()
    return users_controller.create(request)