from flask import Blueprint, request, jsonify
from app import app, db
from app.models.clothes import Clothes
from app.factory.clothes_factory import ClothesFacotry
from app.services.clothes_services import ClothesServices
from app.exceptions.InvalidParamters import InvalidParamtersException
from app.exceptions.NotFound import NotFoundedException

clothes = Blueprint('clothes', __name__, url_prefix="/clothes")

@clothes.route("/create", methods=["POST"])
def create():
    try:
        clothes = ClothesFacotry().create(request.json)
        clothesServices = ClothesServices(clothes)
        clothesServices.save()

        return jsonify({ "message": "Roupa cadastrada com sucesso" }), 200
    except InvalidParamtersException as error:
        return jsonify({ "message": 'Parametros Invalidos' }), 422
    except Exception as error:
        return jsonify({ "message": 'Erro generico' }), 500

@clothes.route("/all", methods=["GET"])
def all():
    try:
        clothesServices = ClothesServices(clothes)
        clothes_list = ClothesFacotry().createList(clothesServices.getAll())

        return jsonify(clothes_list), 200
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

        clothesServices.update(clothes, new_clothes)

        return jsonify({ "message": "Roupa apagada com sucesso" }), 200
    except NotFoundedException as erro:
        return jsonify({ "message": "Roupa não encontrada" }), 404
    except InvalidParamtersException as error:
        return jsonify({ "message": 'Parametros Invalidos' }), 422
    except Exception as erro:
        print(erro)
        return jsonify({ "message": 'Erro generico' }), 500
