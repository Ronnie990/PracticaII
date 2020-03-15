from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("datos.html")
@app.route("/datos")
def datos():
    return render_template("datos.html")
@app.route("/formacion")
def formacion():
    return render_template("formacion.html")
@app.route("/experiencia")
def experiencia():
    return render_template("experiencia.html")
@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")