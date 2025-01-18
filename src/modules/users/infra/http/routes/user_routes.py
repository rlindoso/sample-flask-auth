from flask import Blueprint, jsonify, request
from flask_login import login_required, logout_user
from src.modules.users.infra.http.controllers.sessions_controller import SessionsController
from src.modules.users.infra.http.controllers.users_controller import UsersController

user_route_bp = Blueprint("user_routes", __name__)

def load_user(user_id):
    sessions_controller = SessionsController()
    return sessions_controller.get_user(user_id)

@user_route_bp.route('/login', methods=["POST"])
def login():
    sessions_controller = SessionsController()
    return sessions_controller.create(request)

@user_route_bp.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})

@user_route_bp.route('/user', methods=["POST"])
@login_required
def create_user():
    users_controller = UsersController()
    return users_controller.create(request)

@user_route_bp.route('/user/<string:username>', methods=["GET"])
@login_required
def get_user(username):
    users_controller = UsersController()
    return users_controller.show(request)

@user_route_bp.route('/user/<int:user_id>', methods=["PUT"])
@login_required
def update_user(user_id):
    users_controller = UsersController()
    return users_controller.update(request)

@user_route_bp.route('/user/<int:user_id>', methods=["DELETE"])
@login_required
def delete_user(user_id):
    users_controller = UsersController()
    return users_controller.delete(request)
