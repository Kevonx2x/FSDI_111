from flask import Flask # from 

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Turon",
        "last_name": "Boyd",
        "hobbies": "chess, guitar, cumbia",
        "is_online": True
    }
    return me 

def scan():
    conn = get.db()
    cursor =c conn.execture("SELECT * FROM task WHERE id=?", (task_id))