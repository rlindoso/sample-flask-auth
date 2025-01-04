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
    return db.session.get(ident=user_id, entity=User)

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return jsonify({"message": "Logged in"}), 200
    
    return jsonify({"message": "Invalid username or password"}), 400

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})

@app.route('/user', methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created"})
    
    return jsonify({"message": "Invalid credentials"}), 400

@app.route('/user/<int:id_user>', methods=["GET"])
@login_required
def get_user(id_user):
    user = db.session.get(ident=id_user, entity=User)

    if user:
        return {"username": user.username}

    return jsonify({"message": "User not found"}), 404

@app.route('/user/<int:id_user>', methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = db.session.get(ident=id_user, entity=User)

    if user:
        user.password = data.get("password")
        db.session.commit()
        return {"message": f"User {user.username} updated"}

    return jsonify({"message": "User not found"}), 404

@app.route('/user/<int:id_user>', methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = db.session.get(ident=id_user, entity=User)

    if id_user == current_user.id:
        return jsonify({"message": "deletion not permitted"}), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.username} deleted"}

    return jsonify({"message": "User not found"}), 404


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)