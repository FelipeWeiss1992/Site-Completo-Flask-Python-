from comunidade import app, db
from comunidade.models import Usuario, Post

# with app.app_context():
#     db.create_all()



with app.app_context():
    meus_usuario = Usuario.query.filter_by(email='felipeweiss912@gmail.com').first()
    print(meus_usuario.cursos)



# with app.app_context():
#     meus_usuario = Usuario.query.filter_by(id=3).first()
#     print(meus_usuario)
#     print(meus_usuario.senha)