from flask import render_template,redirect,url_for,flash,request
from comunidadeimpressionadora.forms import FormCriarConta,FormLogin
from comunidadeimpressionadora import app , database , bcrypt
from comunidadeimpressionadora.models import Usuario,Post
from flask_login import login_user

lista_usuarios = ['kennedy', 'mateus','jonatan']


@app.route('/')
def home():
    return render_template('home.html') #usando render_template para chamar o arquivo html 

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)

@app.route('/login_criarconta',methods=['GET','POST']) #formularios tem que liberar os metodos pra uso como o POST
def loginCriarConta():
    formLogin = FormLogin()
    formCriarConta = FormCriarConta()

    if formLogin.validate_on_submit() and 'botao_submit_logar' in request.form:
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha,formLogin.senha.data):
        
            login_user(usuario,remember=formLogin.lembrar_dados.data)
            # para saber qual botão foi clicado importamo o request
            #exibir mensagem de login bem sucedido (import o flash)
            flash(f'Login feito com sucesso com o email {formLogin.email.data}','alert-success')
            # e voltar pra pagina inicial (import o redirect)
            return redirect(url_for('home'))
        else:
            flash('Falha ao logar email ou senha incorretos','alert-danger')
    
    
    
    
    if formCriarConta.validate_on_submit() and 'botao_submit_criarConta' in request.form:
        #criptografando a senha 
        senha_cript = bcrypt.generate_password_hash(formCriarConta.senha.data) 
        #criar um usuario(estancia da classe usuario)
        usuario1 = Usuario(username = formCriarConta.username.data,email=formCriarConta.email.data,senha=senha_cript)
        #adciono sessao 
        database.session.add(usuario1)
        #faço o comit
        database.session.commit()
        
        flash(f'Conta criada com sucesso com o email {formCriarConta.email.data}','alert-success')
        return redirect(url_for('home'))


    return render_template('login_criar_conta.html',formCriarConta=formCriarConta,formLogin=formLogin)