import os
from flask import Flask
from flask.cli import load_dotenv
from flask_cors import CORS
from src.shared.infra.http.routes.routes import register_routes
from src.shared.infra.database.connection import db_connection_handler

load_dotenv()

db_connection_handler.connect_to_db()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default_secret_key")
CORS(app)

register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
