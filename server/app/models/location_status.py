from app import db

class LocationStatus(db.Model):
    __tablename__ = "location_status"

    id = db.Column(db.Integer, primary_key=True)
    location_status = db.Column(db.String(45))

    def __init__(self, location_status):
        self.location_status = location_status

    def __repr__(self):
        return "<LocationStatus %r>" % self.location_status
