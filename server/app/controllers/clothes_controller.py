from flask import Blueprint, request, jsonify
from app import app, db
from app.models.clothes import Clothes
from app.factory.clothes_factory import ClothesFacotry
from app.services.clothes_services import ClothesServices
from app.exceptions.InvalidParamters import InvalidParamtersException

clothes = Blueprint('clothes', __name__, url_prefix="/clothes")

@clothes.route("/create", methods=["POST"])
def create():
    try:
        clothes = ClothesFacotry().create(request.json)
        clothesServices = ClothesServices(clothes)
        clothesServices.save()

        return jsonify({ "message": "Roupa cadastrada com sucesso" }), 200
    except InvalidParamtersException as error:
        return jsonify({ "message": 'Parametros Invalidos' }), 401
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
def get(id):
    try:
        clothesServices = ClothesServices(None)
        clothesServices.delete(id)

        return jsonify({ "message": "Roupa apagada com sucesso" }), 200
    except Exception as erro:
        print(erro)
        return jsonify({ "message": 'Erro generico' }), 500
