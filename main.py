from flask import Flask
from flask import render_template

app = Flask(__name__,
    static_url_path='',
    static_folder='static')


@app.get("/")
def home():
    return render_template("home.html")

@app.get("/sobre")
def about():
    return render_template("about.html")

@app.get("/entrar")
def entrar():
    return render_template("entrar.html")

@app.get("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.get("/painel")
def painel():
    return render_template("painel.html")
