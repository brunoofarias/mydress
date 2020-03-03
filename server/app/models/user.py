from app import db

class User(db.Model):
    __tablename__ = "users"

    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    cpf = db.Column(db.String(14), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
