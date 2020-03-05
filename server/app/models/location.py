from app import db
import datetime

class Location(db.Model):
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key = True)
    locator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    location_status = db.Column(db.Integer, db.ForeignKey('location_status.id'))
    clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.id'))
    final_price = db.Column(db.Float, nullable=False)
    total_days = db.Column(db.Integer, nullable=False)
    payment_status  = db.Column(db.String)
    avaliation_note = db.Column(db.Integer)
    avaliation_text = db.Column(db.Text(500))

    clothes = db.relationship('Clothes', foreign_keys=clothes_id)
    locator = db.relationship('User', foreign_keys=locator_id)
    tenant = db.relationship('User', foreign_keys=tenant_id)
    
    def __init__(self, locator_id, tenant_id, date_start, date_end, location_status, clothes_id, final_price, total_days):
        self.locator_id = locator_id
        self.tenant_id = tenant_id
        self.date_start = date_start
        self.date_end = date_end
        self.location_status = location_status
        self.clothes_id = clothes_id,
        self.final_price = final_price,
        self.total_days = total_days

    def __repr__(self):
        return "<Location %r>" % self.id
