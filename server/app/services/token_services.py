import datetime
import jwt
from dotenv import load_dotenv

load_dotenv()
import os

from app.exceptions.InvalidToken import InvalidTokenException
from app.services.user_services import UserServices

class TokenServices:
    def __init__(self):
        self.secret = os.getenv('SECRET_KEY')

    def createToken(self, user):
        payload = {
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        }

        token = jwt.encode(payload, self.secret)

        return token.decode('utf-8')

    def testToken(self, request):
        if 'authorization' not in request.headers:
            raise InvalidTokenException('Token inválido')
        
        token = request.headers['authorization']
        
        decoded = jwt.decode(token, self.secret)

        userServices = UserServices()
        user = userServices.getUserEmail(decoded['email'])

        return user
