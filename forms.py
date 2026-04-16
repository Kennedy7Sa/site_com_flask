from flask_wtf import FlaskForm #pra criar o formulario 
from wtforms import StringField,PasswordField,SubmitField # criar campos do formulario 
from wtforms.validators import DataRequired,length,Email,equal_to #validar campos 

class FormCriarConta(FlaskForm):
    username= StringField('Nome de usuario',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(),Email()])
    senha= PasswordField('Senha',validators=[DataRequired(),length(6,20)])
    confirmacao= PasswordField('confirmação de senha',validators=[DataRequired(),equal_to('senha')])
    botao_submit_criarConta = SubmitField('Criar conta')


class FormLogin(FlaskForm):
    email= StringField('Digite seu email',validators=[DataRequired(),Email()])
    senha = PasswordField('Digite sua senha',validators=[DataRequired(),length(6,20)])
    botao_submit_logar = SubmitField('Fazer login')