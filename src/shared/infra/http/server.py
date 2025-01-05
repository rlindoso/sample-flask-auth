from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from src.shared.infra.http.routes.routes import register_routes
from src.shared.infra.database.connection import db_connection_handler


db_connection_handler.connect_to_db()

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
CORS(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

register_routes(app)
