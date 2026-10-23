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
