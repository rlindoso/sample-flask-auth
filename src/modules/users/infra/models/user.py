from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from src.shared.infra.database.base import Base

class User(Base, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String(80), nullable=False, default='user')

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password, "role": self.role}