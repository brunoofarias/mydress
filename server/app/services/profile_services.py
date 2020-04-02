from app import db
from app.models.profile import Profile

class ProfileServices:
    def getProfile(self, profile):
        return Profile.query.filter_by(id=profile).first()
