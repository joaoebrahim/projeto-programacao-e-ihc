from flask import Flask
from flask import render_template

app = Flask(__name__,
    static_url_path='',
    static_folder='static')


materias = [
    {
        "id": 1,
        "nome": "Probabilidade e Estatística",
        "professor": "Prof. Marcos Lima",
        "prova": "05/11/2026",
        "horas": 6,
        "acerto": 58
    },
    {
        "id": 2,
        "nome": "Laboratório de Programação III",
        "professor": "Profa. Carla Mendes",
        "prova": "12/11/2026",
        "horas": 4,
        "acerto": 72
    },
    {
        "id": 3,
        "nome": "Interação Humano-Computador",
        "professor": "Prof. Rafael Costa",
        "prova": "19/11/2026",
        "horas": 5,
        "acerto": 85
    },
    {
        "id": 4,
        "nome": "Banco de Dados",
        "professor": "Profa. Juliana Rocha",
        "prova": "26/11/2026",
        "horas": 0,
        "acerto": 0
    },
]


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

@app.get("/materias")
def minhas_materias():
    return render_template("materias.html", materias=materias)
