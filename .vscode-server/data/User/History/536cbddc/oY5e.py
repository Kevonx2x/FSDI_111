from flask import Flask # from 

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name"
    }