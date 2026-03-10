from flask import Flask

app = Flask(__name__)


todo = [
    {"id": 1, "task": "Go shopping", "is_done": False},
    {"id": 2, "task": "Cook dinner", "is_done": False},
]

# TODO 1 - GET endpoint to return all todo items
@app.route("/")
def hello_world():
    return todo




"""
# TODO 2 - Add a new todo to the list using POST
@app.route("/add_to_do/<str:todo_name>", method="POST")
def add_to_do(todo_name):
    print(todo_name)

    www.matthewray.co.uk/add_to_do/baththedog




# TODO 2 - Add a new todo to the list using POST
@app.route("/add_to_do", method="POST")
def add_to_do():
    request.get("todo_name")

    www.matthewray.co.uk/add_to_do/?todo_name=baththedog

"""