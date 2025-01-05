from flask import Blueprint, Flask
from src.modules.users.infra.http.routes.user_routes import user_route_bp


route_bp = Blueprint("routes", __name__)

def register_routes(app: Flask):
    app.register_blueprint(user_route_bp)