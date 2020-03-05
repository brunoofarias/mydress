from app import db
from app.models.clothes import Clothes

class ClothesServices():
    def __init__(self, clothes):
        self.clothes = clothes

    def save(self):
        db.session.add(self.clothes)
        db.session.commit()

        return True

    def getAll(self):
        return Clothes.query.all()

    def getById(self, clothes_id):
        return Clothes.query.filter_by(id=clothes_id).first()
