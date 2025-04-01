from flask import Flask, request, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

# Conectar con la base de datos
def get_db_connection():
    return pymysql.connect(
        host="mysql-db",  
        user="root",
        password="admin",
        database="prueba",
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

 # este metodo 
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        conn.commit()
        return redirect(url_for('index'))  # Redirigir a la misma página después de agregar el usuario

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("index.html", usuarios=usuarios)

@app.route("/eliminar/<int:usuario_id>", methods=["POST"])
def eliminar(usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))  # Redirigir de vuelta a la página de inicio

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# fin.
# fin 2
