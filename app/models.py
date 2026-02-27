from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    nationalite = db.Column(db.String(100), nullable=False)
