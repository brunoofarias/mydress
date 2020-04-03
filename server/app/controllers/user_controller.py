from flask import Blueprint, request, jsonify
from app import app, db
from app.exceptions.InvalidParamters import InvalidParamtersException
from app.exceptions.UserAlreadyExists import UserAlreadyExists
from app.exceptions.UserNotFouded import UserNotFounded
from app.exceptions.InvalidToken import InvalidTokenException
from app.factory.user_factory import UserFactory
from app.services.user_services import UserServices
from app.services.token_services import TokenServices
import datetime

users = Blueprint('users', __name__, url_prefix="/users")

userServices = UserServices()
tokenServices = TokenServices()

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

@users.route("/login", methods=["POST"])
def login():
    try:
        userRequest = UserFactory.createLogin(request.json)
        user = userServices.getUser(userRequest)
 
        UserFactory.verify(user, True)

        token = tokenServices.createToken(user)

        return jsonify({
            "message": "Usuário autenticado",
            "token": token
        }), 200
    except InvalidParamtersException:
        return jsonify({
            "message": "Parametros invalidos"
        }), 422 
    except UserNotFounded:
        return jsonify({
            "message": "Usuário ou senha incorretos"
        }), 401 
    except Exception as error:
        return jsonify({
            "message": "Erro genérico"
        }), 500

@users.route("/test-token", methods=["POST"])
def testToken():
    try:
        user = tokenServices.testToken(request)
        UserFactory.simpleVerify(user)

        return jsonify({
            "message": "Usuário autenticado"
        }), 200
    except InvalidParamtersException:
        return jsonify({
            "message": "Parametros invalidos"
        }), 422 
    except UserNotFounded:
        return jsonify({
            "message": "Usuário ou senha incorretos"
        }), 401 
    except Exception as error:
        return jsonify({
            "message": "Erro genérico"
        }), 500
