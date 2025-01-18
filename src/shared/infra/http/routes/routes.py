from flask import Blueprint, Flask, jsonify
from flask_login import LoginManager
from src.modules.users.infra.http.routes.user_routes import user_route_bp, load_user
from src.shared.errors.error_handler import handle_errors

from src.shared.errors.error_types.http_unauthorized import HttpUnauthorized


route_bp = Blueprint("routes", __name__)

def register_routes(app: Flask):
    app.register_blueprint(user_route_bp)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def manager_user_loader(user_id):
        return load_user(user_id=user_id)
    
    @login_manager.unauthorized_handler
    def handle_exception_unauthorized():
        raise HttpUnauthorized()
    
    @app.errorhandler(Exception)
    def handle_exception(exception):
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code