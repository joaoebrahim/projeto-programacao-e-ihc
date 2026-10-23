from flask import Flask
from flask import abort
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
        "acerto": 58,
        "sessoes": [
            {"data": "13/10/2026", "assunto": "Média e mediana", "tempo": "2 h", "exercicios": 12, "acertos": 7},
            {"data": "16/10/2026", "assunto": "Variância", "tempo": "2 h", "exercicios": 14, "acertos": 8},
            {"data": "20/10/2026", "assunto": "Desvio padrão", "tempo": "2 h", "exercicios": 10, "acertos": 6},
        ]
    },
    {
        "id": 2,
        "nome": "Laboratório de Programação III",
        "professor": "Profa. Carla Mendes",
        "prova": "12/11/2026",
        "horas": 4,
        "acerto": 72,
        "sessoes": [
            {"data": "14/10/2026", "assunto": "Formulários HTML", "tempo": "2 h", "exercicios": 15, "acertos": 11},
            {"data": "21/10/2026", "assunto": "Rotas no Flask", "tempo": "2 h", "exercicios": 10, "acertos": 7},
        ]
    },
    {
        "id": 3,
        "nome": "Interação Humano-Computador",
        "professor": "Prof. Rafael Costa",
        "prova": "19/11/2026",
        "horas": 5,
        "acerto": 85,
        "sessoes": [
            {"data": "15/10/2026", "assunto": "Heurísticas de Nielsen", "tempo": "3 h", "exercicios": 12, "acertos": 10},
            {"data": "22/10/2026", "assunto": "Acessibilidade (WCAG)", "tempo": "2 h", "exercicios": 8, "acertos": 7},
        ]
    },
    {
        "id": 4,
        "nome": "Banco de Dados",
        "professor": "Profa. Juliana Rocha",
        "prova": "26/11/2026",
        "horas": 0,
        "acerto": 0,
        "sessoes": []
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

@app.get("/materia/<int:id>")
def materia(id):
    materia = next((m for m in materias if m["id"] == id), None)
    if materia is None:
        abort(404)
    return render_template("materia.html", materia=materia)

@app.get("/registrar")
def registrar():
    return render_template("registrar.html", materias=materias)

@app.post("/registrar")
def registrar_enviar():
    return render_template("registrar.html", materias=materias, sucesso=True)
