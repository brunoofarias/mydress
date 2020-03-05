from app import db

class Profile(db.Model):
    __tablename__ = "profile"

    id  = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String(100), unique=True)

    def __init__(self, profile):
        self.profile = profile

    def __repr__(self):
        return "<Profile %r>" % self.profile
