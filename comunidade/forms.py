from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from comunidade.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha',validators=[data_required(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Login')