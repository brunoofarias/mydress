from app.utils.utils import Utils
from app.exceptions.InvalidParamters import InvalidParamtersException
from app.exceptions.UserAlreadyExists import UserAlreadyExists
from app.models.user import User
from app.models.profile import Profile
from app.services.profile_services import ProfileServices

profileServices = ProfileServices()

class UserFactory():
    @staticmethod
    def create(data):
        keys = ["name", "email", "cpf", "password", "phone", "image", "profile_type"]
        if (Utils.arrayKeysExists(data, keys) is False):
            raise InvalidParamtersException('Parametros Invalidos')

        profile = profileServices.getProfile(data['profile_type'])

        user = User()
        user.name =  data['name']
        user.email = data['email']
        user.cpf = data['cpf']
        user.password = data['password']
        user.phone = data['phone']
        user.image = data['image']
        user.profile = profile

        return user

    @staticmethod
    def createLogin(data):
        keys = ["email", "password"]
        if (Utils.arrayKeysExists(data, keys)):
            raise InvalidParamtersException('Parametros Invalidos')

        user = User()
        user.email = data['email']
        user.password = data['password']

        return user

    @staticmethod
    def verify(user):
        if user is not None:
            raise UserAlreadyExists('Usuário já existe')
        
