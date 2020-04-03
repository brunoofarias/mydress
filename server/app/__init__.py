from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import profile, user, clothes_types, clothes, clothes_images, location_status, location
from app.controllers.clothes_controller import clothes
from app.controllers.user_controller import users
app.register_blueprint(clothes)
app.register_blueprint(users)
