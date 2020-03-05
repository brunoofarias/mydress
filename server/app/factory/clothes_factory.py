from app.utils.utils import Utils
from app.exceptions.InvalidParamters import InvalidParamtersException
from app.exceptions.NotFound import NotFoundedException
from app.models.clothes import Clothes

class ClothesFacotry():
    @staticmethod
    def create(data):
        if (Utils.arrayKeysExists(data, ['name', 'priceDay', 'locale', 'user_id', 'type_id', 'avaliable']) is False):
            raise InvalidParamtersException('Parametros Invalidos')

        clothes = Clothes(
            data['name'],
            data['priceDay'],
            data['locale'],
            data['user_id'],
            data['type_id'],
            data['avaliable']
        )

        return clothes

    @staticmethod
    def createList(data):
        clothes_list = []

        if data:
            for clothes in data:
                clothes_list.append({
                    "name": clothes.name,
                    "priceDay": clothes.priceDay,
                    "locale": clothes.locale,
                    "user_id": clothes.user_id,
                    "type_id": clothes.type_id,
                    "avaliable": clothes.avaliable,
                })

        return clothes_list

    @staticmethod
    def createOne(clothes):
        return {
            "name": clothes.name,
            "priceDay": clothes.priceDay,
            "locale": clothes.locale,
            "user_id": clothes.user_id,
            "type_id": clothes.type_id,
            "avaliable": clothes.avaliable,
        }

    @staticmethod
    def verify(clothes):
        if (clothes is None):
            raise NotFoundedException('Roupa não encontrada')
