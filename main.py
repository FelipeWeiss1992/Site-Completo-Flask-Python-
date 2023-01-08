from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_pyfile("config.py")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/login', methods = ['GET','POST'])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit() and 'botao_submit_login' in  request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}','alert-success')
        return redirect(url_for('home'))


    return render_template('login.html', form_login = form_login)
    
@app.route('/criar_conta', methods = ['GET','POST'])
def criar_conta():
    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))


    return render_template('criar_conta.html', form_criarconta = form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)