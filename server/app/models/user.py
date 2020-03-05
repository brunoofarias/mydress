from app import db
import datetime

class User(db.Model):
    __tablename__ = "users"

    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    cpf = db.Column(db.String(14), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    date_created = db.Column(db.DateTime)
    phone = db.Column(db.String(20))
    profile_id = db.Column(db.Integer(), db.ForeignKey('profile.id'))
    image = db.Column(db.Text)
    
    profile = db.relationship('Profile', foreign_keys=profile_id)

    def __init__(self, name, email, cpf, password):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.password = password
        self.date_created = datetime.datetime.now()
        self.phone = ""
        self.image = ""

    def __repr__(self):
        return "<User %r>" % self.name
        