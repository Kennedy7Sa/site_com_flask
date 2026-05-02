from flask import render_template,redirect,url_for,flash,request

from comunidadeimpressionadora.forms import FormCriarConta,FormLogin,FormEditarPerfil,FormCriarPost
from comunidadeimpressionadora import app , database , bcrypt
from comunidadeimpressionadora.models import Usuario,Post
from flask_login import login_user,logout_user , current_user,login_required
import secrets
import os
from PIL import Image




@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())
    return render_template('home.html',posts=posts) #usando render_template para chamar o arquivo html 

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
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
            parametro_next = request.args.get('next') #pra pegar o parametro da url pra mandar o usuario pra pagina escolhida apos login
            if parametro_next:
                return redirect(parametro_next)
            else:            
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


#parte do usuario logado 
@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso','alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static',filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('perfil.html',foto_perfil=foto_perfil)

@app.route('/post/criar',methods=['GET','POST'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo = form.titulo.data,corpo = form.corpo.data,autor = current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso','alert-success')
        return redirect(url_for('home'))

    return render_template('criarpost.html',form=form)



def salvar_imagem(imagem):
    #adcionar codigo no nome da image 
    codigo = secrets.token_hex(8)
    nome , extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome+codigo+extensao
    caminho_completo = os.path.join(app.root_path , 'static/fotos_perfil',nome_arquivo)
            # reduzir tamanho 
    tamanho = (200,200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    #salvar foto
    imagem_reduzida.save(caminho_completo)
             
            #mudar a foto de perfil do usuario 
    return nome_arquivo

def atualizar_cursos(formulario):
    lista_cursos = []
    for campo in formulario:
        if campo.data:
            if 'curso_' in campo.name:
                lista_cursos.append(campo.label.text)
           
    return ';'.join(lista_cursos)




@app.route('/perfil/editar',methods=['GET','POST'])
@login_required
def editarPerfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form)
            
        database.session.commit()
        flash('Perfil atualizado com sucesso ','alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.username.data = current_user.username


    foto_perfil = url_for('static',filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('editarperfil.html',foto_perfil=foto_perfil,form = form)
    

