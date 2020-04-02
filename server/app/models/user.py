from app import db
import datetime

class User(db.Model):
    __tablename__ = "users"

    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    cpf = db.Column(db.String(14), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    phone = db.Column(db.String(20))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    image = db.Column(db.Text)
    
    profile = db.relationship('Profile', foreign_keys=profile_id)

    def __repr__(self):
        return "<User %r>" % self.name

    
        