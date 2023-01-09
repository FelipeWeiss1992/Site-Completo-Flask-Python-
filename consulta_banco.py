from comunidade import app, db
from comunidade.models import Usuario, Post

# with app.app_context():
#     db.create_all()



with app.app_context():
    meus_usuario = Usuario.query.first()
    print(meus_usuario)



# with app.app_context():
#     meus_usuario = Usuario.query.filter_by(id=3).first()
#     print(meus_usuario)
#     print(meus_usuario.senha)