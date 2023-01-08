from comunidade import app, db
from comunidade.models import Usuario, Post

with app.app_context():
    db.create_all()