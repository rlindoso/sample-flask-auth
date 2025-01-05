from database import db
from flask_login import UserMixin
from src.shared.infra.database.base import Base

class User(Base, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')