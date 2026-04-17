from flask import Flask,render_template, url_for,request,flash,redirect
from forms import FormLogin,FormCriarConta

app = Flask(__name__)
lista_usuarios = ['kennedy', 'mateus','jonatan']
app.config['SECRET_KEY'] = 'a3ff4c3b25f04b163a48caa8afc3e869'


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

    if formLogin.validate_on_submit and 'botao_submit_logar' in request.form:
         # para saber qual botão foi clicado importamo o request
        #exibir mensagem de login bem sucedido (import o flash)
        flash(f'Login feito com sucesso com o email {formLogin.email.data}','alert-success')
        # e voltar pra pagina inicial (import o redirect)
        return redirect(url_for('home'))
    if formCriarConta.validate_on_submit and 'botao_submit_criarConta' in request.form:
        flash(f'Conta criada com sucesso com o email {formCriarConta.email.data}','alert-success')
        return redirect(url_for('home'))


    return render_template('login_criar_conta.html',formCriarConta=formCriarConta,formLogin=formLogin)

if __name__ == '__main__':
    app.run(debug=True) #toda mudança ja é implementada sempre que houver uma edição 
#teste