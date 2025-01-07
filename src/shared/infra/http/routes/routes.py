from flask import Blueprint, Flask, jsonify
from src.modules.users.infra.http.routes.user_routes import user_route_bp
from src.shared.errors.error_handler import handle_errors


route_bp = Blueprint("routes", __name__)

def register_routes(app: Flask):
    app.register_blueprint(user_route_bp)
    
    @app.errorhandler(Exception)
    def handle_exception(exception):
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code