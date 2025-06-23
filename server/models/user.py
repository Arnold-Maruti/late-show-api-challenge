from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from . import db

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    
    @property
    def password(self):
        raise AttributeError("Password cannot be accessed directly.")

    @password.setter
    def password(self, password_plaintext):
        self.password_hash = generate_password_hash(password_plaintext)

    def authenticate(self, password_plaintext):
        return check_password_hash(self.password_hash, password_plaintext)


