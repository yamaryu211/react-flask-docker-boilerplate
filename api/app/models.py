from app import db
from flask import Blueprint

models_blueprint = Blueprint('app',__name__)

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):

        return f"Puppy {self.name} is {self.age} years old."

class Kitty(db.Model):

    __tablename__ = 'kitties'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):

        return f"Kitty {self.name} is {self.age} years old."
