from flask import Blueprint, request, jsonify
from app import app, db
from app.models.clothes import Clothes
from app.factory.clothes_factory import ClothesFacotry
from app.factory.user_factory import UserFactory
from app.services.clothes_services import ClothesServices
from app.exceptions.InvalidParamters import InvalidParamtersException
from app.exceptions.InvalidToken import InvalidTokenException
from app.exceptions.NotFound import NotFoundedException
from app.exceptions.UserNotFouded import UserNotFounded
from app.services.token_services import TokenServices

clothes = Blueprint('clothes', __name__, url_prefix="/clothes")

tokenServices = TokenServices()

@clothes.route("/create", methods=["POST"])
def create():
    try:
        clothes = ClothesFacotry().create(request.json)
        clothesServices = ClothesServices(clothes)
        clothe = clothesServices.save()

        return jsonify({ 
            "message": "Roupa cadastrada com sucesso",
            "clothe": {
                "id": clothe.id,
                "name": clothe.name,
                "priceDay": clothe.priceDay,
                "locale": clothe.locale,
                "user_id": clothe.user_id,
                "type_id": clothe.type_id,
                "avaliable": clothe.avaliable,
            }
        }), 200
    except InvalidParamtersException as error:
        return jsonify({ "message": 'Parametros Invalidos' }), 422
    except Exception as error:
        return jsonify({ "message": 'Erro generico' }), 500

@clothes.route("/all", methods=["GET"])
def all():
    try:
        user = tokenServices.testToken(request)
        UserFactory.simpleVerify(user)

        clothesServices = ClothesServices(clothes)
        clothes_list = ClothesFacotry().createList(clothesServices.getAll())

        return jsonify(clothes_list), 200
    except InvalidParamtersException:
        return jsonify({
            "message": "Parametros invalidos"
        }), 422
    except InvalidTokenException:
        return jsonify({
            "message": "Token Inválido"
        }), 401
    except Exception as erro:
        print(erro)
        return jsonify({ "message": 'Erro generico' }), 500

@clothes.route("/<id>", methods=["GET"])
def get(id):
    try:
        clothesServices = ClothesServices(None)
        clothes = ClothesFacotry().createOne(clothesServices.getById(id))

        return jsonify(clothes), 200
    except Exception as erro:
        print(erro)
        return jsonify({ "message": 'Erro generico' }), 500

@clothes.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    try:
        clothesServices = ClothesServices(None)
        clothes = clothesServices.getById(id)

        ClothesFacotry().verify(clothes)

        clothesServices.delete(clothes)

        return jsonify({ "message": "Roupa apagada com sucesso" }), 200
    except NotFoundedException as erro:
        return jsonify({ "message": "Roupa não encontrada" }), 404
    except Exception as erro:
        print(erro)
        return jsonify({ "message": 'Erro generico' }), 500

@clothes.route("/update/<id>", methods=["PUT"])
def update(id):
    try:
        new_clothes = ClothesFacotry().create(request.json)

        clothesServices = ClothesServices(None)
        clothes = clothesServices.getById(id)

        ClothesFacotry().verify(clothes)

        clothes_updated = clothesServices.update(clothes, new_clothes)

        return jsonify({ 
            "message": "Roupa alterada com sucesso",
            "clothe": {
                "id": clothes_updated.id,
                "name": clothes_updated.name,
                "priceDay": clothes_updated.priceDay,
                "locale": clothes_updated.locale,
                "user_id": clothes_updated.user_id,
                "type_id": clothes_updated.type_id,
                "avaliable": clothes_updated.avaliable,
            }
        }), 200
    except NotFoundedException as erro:
        return jsonify({ "message": "Roupa não encontrada" }), 404
    except InvalidParamtersException as error:
        return jsonify({ "message": 'Parametros Invalidos' }), 422
    except Exception as erro:
        print(erro)
        return jsonify({ "message": 'Erro generico' }), 500
