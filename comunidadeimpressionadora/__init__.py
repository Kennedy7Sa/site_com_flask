from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a3ff4c3b25f04b163a48caa8afc3e869'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
 
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'loginCriarConta'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes