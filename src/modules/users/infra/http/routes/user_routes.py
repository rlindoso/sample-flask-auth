from flask import Blueprint, request
from src.modules.users.infra.http.controllers.sessions_controller import SessionsController

user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route('/login', methods=["POST"])
def login():
    sessions_controller = SessionsController()
    return sessions_controller.create(request)
