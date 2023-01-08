from comunidade import app,db
from flask import render_template, redirect, flash, request, url_for
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

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
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=form_criarconta.senha.data)
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('home'))


    return render_template('criar_conta.html', form_criarconta = form_criarconta)