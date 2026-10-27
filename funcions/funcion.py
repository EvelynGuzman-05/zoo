import mysql.connector

def db_conexion(sql, params=(), fetch=False):
    conn = mysql.connector.connect(host="db", user="animal", password="animalito123", database="zoo")
    cur = conn.cursor(dictionary=True)
    cur.execute(sql, params)
    rows = cur.fetchall() if fetch else None
    conn.commit()
    conn.close()
    return rows


def agregar(nombre, color, especie):
    db_conexion("INSERT INTO animales (nombre, color, especie) VALUES (%s, %s, %s)",
       (nombre, color, especie))
    return True  

def eliminar(id):
    db_conexion("DELETE FROM animales WHERE id = %s", (id,))
    return True

def editar(id, nombre, color, especie):
    db_conexion("UPDATE animales SET nombre = %s, color = %s, especie = %s WHERE id = %s",
       (nombre, color, especie, id))
    return True

def todos_animales():
    return db_conexion("SELECT * FROM animales", fetch=True)
    


