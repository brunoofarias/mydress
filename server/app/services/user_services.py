from app import db
from sqlalchemy import or_
from app.models.user import User

class UserServices:
    def save(self, user):
        db.session.add(user)
        db.session.commit()

        return user

    def getUser(self, user):
        user_exists = User.query.filter(
            email=user.email,
            password=user.password
        )

        return user_exists

    def userExists(self, user):
        user_exists = db.session.query(User).filter(
            or_(
                User.email==user.email,
                User.cpf==user.cpf
            )
        ).first()

        return user_exists
