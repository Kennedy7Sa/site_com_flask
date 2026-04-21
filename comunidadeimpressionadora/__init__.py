from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a3ff4c3b25f04b163a48caa8afc3e869'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
 
database = SQLAlchemy(app)

from comunidadeimpressionadora import routes