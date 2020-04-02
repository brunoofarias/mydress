from flask import Blueprint, request, jsonify
from app import app, db
from app.exceptions.InvalidParamters import InvalidParamtersException
from app.exceptions.UserAlreadyExists import UserAlreadyExists
from app.factory.user_factory import UserFactory
from app.services.user_services import UserServices
import datetime

users = Blueprint('users', __name__, url_prefix="/users")

userServices = UserServices()

@users.route("/create", methods=["POST"])
def create():
    try:
        userRequest = UserFactory.create(request.json)
        userExists = userServices.userExists(userRequest)

        UserFactory.verify(userExists)

        user = userServices.save(userRequest)

        return jsonify({
            "message": "Usuário Cadastrado com sucesso",
            "user": user.id
        }), 200
    except InvalidParamtersException:
        return jsonify({
            "message": "Parametros invalidos"
        }), 422
    except UserAlreadyExists:
        return jsonify({
            "message": "Usuário já existe"
        }), 401
    except Exception as error:
        print(error)
        return jsonify({
            "message": "Erro genérico"
        }), 500
    