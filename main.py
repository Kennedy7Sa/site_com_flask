from flask import Flask,render_template

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True) #toda mudança ja é implementada sempre que houver uma edição 
#teste