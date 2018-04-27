# flask application
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get('HEROKU'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventDatabase.db'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# login
from os import urandom
app.config['SECRET_KEY'] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth_login'
login_manager.login_message = 'Kirjaudu sisään käyttääksesi tätä toiminnallisuutta.'

# roles in login_required
from functools import wraps

def login_required(role='ANY'):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != 'ANY':
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

from application.people import models

from application.series import models

from application.history import models

from application.registration import models

from application.results import models

from application.auth import models

from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# creating the database tables
try:
    db.create_all()
except:
    pass

# application functions
from application import views

from application.people import views

from application.series import views

from application.results import views

from application.auth import views
