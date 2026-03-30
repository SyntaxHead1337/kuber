from flask import Flask
import pymysql

app = Flask(__name__)

# base route for all API endpoints
BASE_ROUTE = "/api"

def get_connection():
    return pymysql.connect(
        host="mariadb",  # Service-Name in k8s
        user="user",
        password="password",
        database="mydb"
    )

@app.route(BASE_ROUTE)
def home():
    return "Flask + MariaDB läuft 🚀"

@app.route(f"{BASE_ROUTE}/init")
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

@app.route(f"{BASE_ROUTE}/add/<name>")
def add_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO test (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()
    
    return f"Added {name}!"

@app.route(f"{BASE_ROUTE}/get")
def get_names():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name FROM test")
    results = cursor.fetchall()
    conn.close()
    
    return {"results": [{"id": r[0], "name": r[1]} for r in results]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
