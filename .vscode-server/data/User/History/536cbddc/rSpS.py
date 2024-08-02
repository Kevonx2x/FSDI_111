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


    statement = """
    INSERT INTO task (
    name,
    summary, description
    ) VALUES (?,?,?)
    """
    conn = get_db()
    conn.execute(statement, task,_tuple)
    conn.commit()

    def update_by_id(task_data, task_id):
        task_tuple