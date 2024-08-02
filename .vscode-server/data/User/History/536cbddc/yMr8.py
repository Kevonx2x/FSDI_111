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

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DTATBASE_URL)
    return db 
        