from app import db

class Clothes(db.Model):
    __tablename__ = "clothes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    priceDay = db.Column(db.Float)
    locale = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('clothes_type.id'))
    avaliable = db.Column(db.Boolean)

    user = db.relationship('User', foreign_keys=user_id)
    clothes_type = db.relationship('ClotheTypes', foreign_keys=type_id)
    clothes_image = db.relationship('ClothesImages', backref="clothes",  lazy=True)

    def __init__(self, name, priceDay, locale, user_id, type_id, avaliable = False):
        self.name = name
        self.priceDay = priceDay
        self.locale = locale
        self.user_id = user_id
        self.type_id = type_id
        self.avaliable = avaliable

    def __repr__(self):
        return "<Clothes %r>" % self.name
