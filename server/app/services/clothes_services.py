from app import db
from app.models.clothes import Clothes

class ClothesServices():
    def __init__(self, clothes):
        self.clothes = clothes

    def save(self):
        db.session.add(self.clothes)
        db.session.commit()

        return self.clothes

    def getAll(self):
        return Clothes.query.all()

    def getById(self, clothes_id):
        return Clothes.query.filter_by(id=clothes_id).first()

    def delete(self, clothes):
        db.session.delete(clothes)
        db.session.commit()

    def update(self, clothes, new_clothes):
        clothes.name = new_clothes.name
        clothes.priceDay = new_clothes.priceDay
        clothes.locale = new_clothes.locale
        clothes.user_id = new_clothes.user_id
        clothes.type_id = new_clothes.type_id
        clothes.avaliable = new_clothes.avaliable

        db.session.commit()

        return clothes

