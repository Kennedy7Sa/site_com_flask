from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/contato')
def contato():
    return 'Qualquer duvida entre em contato om kennedy'

if __name__ == '__main__':
    app.run(debug=True) #toda mudança ja é implementada sempre que houver uma edição 
#teste