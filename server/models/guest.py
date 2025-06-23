from . import db
from sqlalchemy_serializer import SerializerMixin

class Guest(db.Model,SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

