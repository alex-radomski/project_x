from flaskr.main import app


def test_get_todos() -> None:
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json == [
            {"id": 1, "task": "Go shopping", "is_done": False},
            {"id": 2, "task": "Cook dinner", "is_done": False},
        ]

def test_add_todo() -> None:
    with app.test_client() as client:
        
        add_todo_json = {"id": 3, "task": "Read a book", "is_done": False}
        
        response = client.post("/add-todo", json=add_todo_json)

        assert response.status_code == 201
        assert response.json == add_todo_json


def test_add_todo_2() -> None:
    with app.test_client() as client:
        
        add_todo_json = {"id": 4, "task": "Have a bath", "is_done": False}
        
        response = client.post("/add-todo", json=add_todo_json)

        assert response.status_code == 201
        assert response.json == add_todo_json

        get_response = client.get("/")
        assert get_response.status_code == 200
        assert get_response.json == [
            {"id": 1, "task": "Go shopping", "is_done": False},
            {"id": 2, "task": "Cook dinner", "is_done": False},
            {"id": 3, "task": "Read a book", "is_done": False},
            {"id": 4, "task": "Have a bath", "is_done": False}
        ]


def test_add_todo_invalid_1() -> None:
     with app.test_client() as client:
       response = client.post("/add-todo", json="This is not a dictionary")
       assert response.status_code == 400
        







# ALEX TESTING
def test_create_user():
    with app.test_client() as client:
        add_user_json = {"id": 1, "user": "Harry Potter"}
        response = client.post("/add-user", json=add_user_json)

        assert response.status_code == 201
        assert response.json == add_user_json
