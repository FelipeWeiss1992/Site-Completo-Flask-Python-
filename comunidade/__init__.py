from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET-KEY'] = '29cefg8Bht6kjgotiaN854HJU'
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

from comunidade import views