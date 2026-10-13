import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def db(sql, params=(), fetch=False):
    conn = mysql.connector.connect(host="db", user="zoo_user", password="zoo_pass", database="zoo")
    cur = conn.cursor(dictionary=True)
    cur.execute(sql, params)
    rows = cur.fetchall() if fetch else None
    conn.commit()
    conn.close()
    return rows


@app.route("/")
def index():
    return render_template("index.html", animales=db("SELECT * FROM animales", fetch=True))


@app.route("/agregar", methods=["POST"])
def agregar():
    f = request.form
    db("INSERT INTO animales (nombre, color, especie) VALUES (%s, %s, %s)",
       (f["nombre"], f["color"], f["especie"]))
    return redirect("/")


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    db("DELETE FROM animales WHERE id = %s", (id,))
    return redirect("/")


@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    f = request.form
    db("UPDATE animales SET nombre = %s, color = %s, especie = %s WHERE id = %s",
       (f["nombre"], f["color"], f["especie"], id))
    return redirect("/")


if __name__ == '__main__':

    app.run()