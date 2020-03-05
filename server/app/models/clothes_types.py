from app import db

class ClotheTypes(db.Model):
    __tablename__ = "clothes_type"

    id = db.Column(db.Integer, primary_key=True)
    clothes_type = db.Column(db.String(45))

    def __init__(self, clothes_type):
        self.clothes_type = clothes_type

    def __repr__(self):
        return "<ClothesType %r>" % self.clothes_type
        