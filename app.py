from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager, login_required, login_user, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Logged in"}), 200
    
    return jsonify({"message": "Invalid username or password"}), 400

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)