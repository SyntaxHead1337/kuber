from flask import Flask
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host="mariadb",
        user="user",
        password="password",
        database="mydb"
    )

@app.route("/")
def home():
    return "Flask + MariaDB läuft 🚀"

@app.route("/init")
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    """)

    conn.commit()
    conn.close()
    return "Table created!"

@app.route("/add/<name>")
def add(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO test (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

    return f"{name} added!"

@app.route("/get")
def get():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM test")
    result = cursor.fetchall()

    conn.close()
    return str(result)
