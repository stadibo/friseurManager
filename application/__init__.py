from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
import os

import os

# database

# if os.environ.get("HEROKU"):
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
# else:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friseur.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# application
from application import views

from application.auth import views
from application.auth import models

from application.appointments import models

from application.work_days import models

# login functionality
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database table creation
try:
    db.create_all()
except:
    pass
