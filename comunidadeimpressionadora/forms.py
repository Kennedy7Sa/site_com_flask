from flask_wtf import FlaskForm #pra criar o formulario 
from wtforms import StringField,PasswordField,SubmitField,BooleanField # criar campos do formulario 
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired,Length,Email,ValidationError,EqualTo #validar campos 
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username= StringField('Nome de usuario',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(),Email()])
    senha= PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
    confirmacao= PasswordField('confirmação de senha',validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarConta = SubmitField('Criar conta')

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if usuario:
            raise ValidationError('Esse email já esxiste ! coloque outro email ou faça login ')



class FormLogin(FlaskForm):
    email= StringField('Digite seu email',validators=[DataRequired(),Email()])
    senha = PasswordField('Digite sua senha',validators=[DataRequired(),Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_logar = SubmitField('Fazer login')


class FormEditarPerfil(FlaskForm):
    username= StringField('Nome de usuario',validators=[DataRequired()])
    email= StringField('Digite seu email',validators=[DataRequired(),Email()])
    foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg','png'])])
    curso_excel = BooleanField("Excel impressionador")
    curso_vba = BooleanField("vba impressionador")
    curso_powerbi = BooleanField("power bi impressionador")
    curso_ppt = BooleanField("ppt impressionador")
    curso_python = BooleanField("python impressionador")
    curso_sql = BooleanField("sql impressionador")
    botao_submit_editarPerfil = SubmitField('Confirmar edição')
    
    def validate_email(self,email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email= email.data).first()
            if usuario:
                raise ValidationError('Esse email já esxiste ! coloque outro email para edição')