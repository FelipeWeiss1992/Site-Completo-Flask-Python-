from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cefg8Bht6kjgotiaN854HJU'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

db = SQLAlchemy(app)

from comunidade import views