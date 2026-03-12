from flask import Flask
from flask import request

app = Flask(__name__)


todo = [
    {"id": 1, "task": "Go shopping", "is_done": False},
    {"id": 2, "task": "Cook dinner", "is_done": False},
]

# TODO 1 - GET endpoint to return all todo items
@app.route("/")
def hello_world():
    return todo

@app.route("/add_todo", methods=["POST"])
def add_todo() -> dict:
    req = request.get_json()
    
    if type(req) != dict:
        return "", 400

    
    
    
    todo.append(req)
    return req, 201
