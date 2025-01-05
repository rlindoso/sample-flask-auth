from bcrypt import checkpw
from flask import Blueprint, jsonify, request
from flask_login import login_user
from src.modules.users.infra.http.controllers.sessions_controller import SessionsController
from src.modules.users.infra.models.repositories.userRepository import UserRepository
from src.shared.infra.database.connection import db_connection_handler

from src.modules.users.infra.models.user import User

user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route('/login', methods=["POST"])
def login():
    sessions_controller = SessionsController()
    return sessions_controller.create(request)
