from . import db
from sqlalchemy_serializer import SerializerMixin

class Guest(db.Model,SerializerMixin):
    __tablename__ = 'guests'
    serialize_rules = ('-appearances',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    occupation = db.Column(db.String(), nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

