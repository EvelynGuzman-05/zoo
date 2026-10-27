import mysql.connector
from flask import Flask, render_template, request, redirect
from funcions import funcion as zoo
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", animales=all_animales())


@app.route("/agregar", methods=["POST"])
def agregar():
    f = request.form
    zoo.agregar(f["nombre"], f["color"], f["especie"])
    return redirect("/")


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    zoo.eliminar(id)
    return redirect("/")


@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    f = request.form
    zoo.editar(id, f["nombre"], f["color"], f["especie"])
    return redirect("/")


if __name__ == '__main__':

    app.run()