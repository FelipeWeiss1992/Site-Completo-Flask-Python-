from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['Lira', 'Felipe', 'Maiara']

app.config['SECRET_KEY'] = '71a998e3507079eab097eda8bcd034aa'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    return render_template('login.html', form_login = form_login)
    
@app.route('/criar_conta')
def criar_conta():
    form_criarconta = FormCriarConta()
    return render_template('criar_conta.html', form_criarconta = form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)