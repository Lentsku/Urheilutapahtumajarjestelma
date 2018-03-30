# flask application
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventDatabase.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# application functions
from application import views

from application.people import models
from application.people import views

from application.series import models
from application.series import views

from application.auth import models
from application.auth import views

# login
from application.auth.models import User
from os import urandom
app.config['SECRET_KEY'] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth_login'
login_manager.login_message = 'Kirjaudu sisään käyttääksesi tätä toiminnallisuutta.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# creating the database tables
db.create_all()
