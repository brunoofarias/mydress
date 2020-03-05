from app import db

class ClothesImages(db.Model):
    __tablename__ = "clothe_images"

    id = db.Column(db.Integer, primary_key=True)
    clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.id'))
    image_url = db.Column(db.String(250))

    def __init__(self, clothes_id, image_url):
        self.clothes_id = clothes_id
        self.image_url = image_url

    def __repr__(self):
        return "<ClothesImages %r>" % self.id
