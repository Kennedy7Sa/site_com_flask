from flask_wtf import FlaskForm #pra criar o formulario 
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField # criar campos do formulario 
from wtforms.validators import DataRequired,Length,Email,EqualTo #validar campos 

class FormCriarConta(FlaskForm):
    username= StringField('Nome de usuario',validators=[DataRequired()])
    email= EmailField('Email',validators=[DataRequired(),Email()])
    senha= PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
    confirmacao= PasswordField('confirmação de senha',validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarConta = SubmitField('Criar conta')


class FormLogin(FlaskForm):
    email= EmailField('Digite seu email',validators=[DataRequired(),Email()])
    senha = PasswordField('Digite sua senha',validators=[DataRequired(),Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_logar = SubmitField('Fazer login')