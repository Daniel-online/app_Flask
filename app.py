from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)
@app.route("/Acesso")
def Acesso():
    return render_template('index.html')
@app.route("/registrar_usuario", methods= ["POST"] )
def registrar_usuario():
    user_name = request.form['nome_usuario']
    user_mail = request.form['email_usuario']
    user_phone = request.form['tel_usuario']
    user_password = request.form['senha_usuario']

    #inserir conexão com o sql aqui

    return render_template('agradecimento_cadastro.html')
    
@app.route("/")
def index():
    return 'Index Page <br> <a href="http://127.0.0.1:5000/Acesso">Cadastre-se</a>'

@app.route("/user/<user_name>")
def show_user_name(user_name):
    return f'User:  {escape(user_name)}'

@app.route('/post/<post_id>')
def show_post(post_id):
    return f'Post: {post_id}'
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath{escape(subpath)}'

#ordenar o array de cadastros

@app.route("/hello")
def hello_world():
    return "<p>Hello. World!</p>  "

if __name__ == '__main__':
    app.run(debug=True)