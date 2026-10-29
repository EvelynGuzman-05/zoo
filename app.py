import mysql.connector
from flask import Flask, render_template, request, redirect
from functions import function as zoo
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", animales=zoo.all_animals())


@app.route("/add", methods=["POST"])
def add():
    f = request.form
    zoo.add_animal(f["nombre"], f["color"], f["especie"])
    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    zoo.delete_animal(id)
    return redirect("/")


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    f = request.form
    zoo.update_animal(id, f["nombre"], f["color"], f["especie"])
    return redirect("/")


if __name__ == '__main__':

    app.run()