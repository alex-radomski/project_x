import uuid

from flask import Flask, redirect, render_template, render_template_string, request, url_for
from markupsafe import escape
from pydantic import BaseModel, ValidationError

# import flaskr.todo_list_database as todo
# import flaskr.user_database as user_db

app = Flask(__name__)


class ToDo(BaseModel):
    # model_config = {
    #     "extra": "forbid"}

    id: str
    task: str
    is_done: bool


class User(BaseModel):
    id: int
    user: str


# [{id:name},...]
user_db: list[User] = []

# [{id:int,task:name,is_done:bool},...]
todo = [
    {
        "id": "fe8fc3f6-29fc-400c-9ec1-77557417e811",
        "task": "Feed the dog",
        "is_done": True,
    },
    {
        "id": "d157cbe5-4242-446a-9dea-896747f24c52",
        "task": "Cook dinner",
        "is_done": False,
    },
    {
        "id": "982d4092-455a-49f4-8d5f-f58df7341d08",
        "task": "Read a book",
        "is_done": False,
    },
]


# GET endpoint to return all todo items
@app.route("/")
def hello_world():
    return render_template("home.html", todo_list=todo, user_list=user_db)


# POST endpoint that accepts a json obj and adds it to todo
@app.route("/add-todo", methods=["POST"])
def add_todo():
    form_task = request.form.get("task")
    form_is_done = request.form.get("is_done",False)

    try:
        todo_req = ToDo(id=str(uuid.uuid4()), task=form_task, is_done=form_is_done)
    except (ValidationError, TypeError, KeyError):
        return "get your shit together", 422
    else:
        valid_dict = todo_req.model_dump()

    todo.append(valid_dict)

    return redirect(url_for('hello_world'))


# GET endpoint that returns all users
@app.route("/users")
def get_users():
    return user_db


# POST endpoint that creates a new user from request JSON
@app.route("/add-user", methods=["POST"])
def create_user():
    req = request.get_json()
    try:
        validate_request = User.model_validate(req)
    except ValidationError:
        return "get your shit together", 422
    else:
        valid_dict = validate_request.model_dump()

    for user in user_db:
        if valid_dict["id"] == user["id"]:
            return "", 422

    user_db.append(valid_dict)
    return valid_dict, 201


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
