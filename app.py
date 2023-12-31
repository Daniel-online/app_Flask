from flask import Flask, render_template, request
from markupsafe import escape
import random
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)    

@app.route("/Acesso")
def Acesso():
    return render_template('index.html')
@app.route("/registrar_usuario", methods= ["GET","POST"] )
def registrar_usuario():
    user_name = request.form['nome_usuario']
    user_mail = request.form['email_usuario']   
    user_phone = request.form['tel_usuario']
    user_password = request.form['senha_usuario']

    #inserir conexão com o sql aqui

    return render_template('agradecimento_cadastro.html')
def gerar_chave():
    cod1 = random.randint()
    cod2 = random.randint()
    cod3 = random.randint()
    cod4 = random.randint()
    cod5 = random.randint()
    list_cod = [cod1, cod2, cod3, cod4, cod5] 
    return  list_cod
#uma chave é composta de 5 códigos gerados aleatoriamente
@app.route("/")
def index():
    return 'Index Page <br> <a href="http://127.0.0.1:5000/Acesso">Cadastre-se</a>'

@app.route("/user/<user_name>")
def show_user_name(user_name):
    return f'User:  {escape(user_name)}'


@app.route('verificar_cadastro')
def acessar_verif_cadastro():
    return("/verificar_cadastro.html")

def verificar_cadastro():
    def validar_codigos():
        if(cod1):
            if(cod2):
                if cod3():
                    if cod4():
                        if cod5():
                            return render_template("")
                        else:
                            flash("Código está incorreto")    
                else:
                    flash("Código está incorreto")
            else:
                flash("Código está incorreto")
        else:
            flash("Código está incorreto")
          


@app.route("/recupera_senha", methods= ["POST"] )
def recuper_senha():
    return render_template("recuperarsenha.html")
