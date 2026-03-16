import pytest

from flaskr.main import app
import flaskr.main as main


@pytest.fixture(autouse=True)
def setup_todos():
    main.todo.clear()
    main.user_db.clear()



# def test_get_todos() -> None:
#     with app.test_client() as client:
#         response = client.get("/")
#         assert response.status_code == 200
#         assert response.json == [
#             {"id": 1, "task": "Go shopping", "is_done": False},
#             {"id": 2, "task": "Cook dinner", "is_done": False},
#         ]

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

        # get_response = client.get("/")
        # assert get_response.status_code == 200
        # assert get_response.json == [
        #     {"id": 4, "task": "Have a bath", "is_done": False}
        # ]


def test_add_todo_invalid_1() -> None:
     with app.test_client() as client:
       response = client.post("/add-todo", json="This is not a dictionary")
       assert response.status_code == 422

def test_add_todo_invalid_2() -> None:
     json_request = {"id": 4, "task": "Go shopping"}
     with app.test_client() as client:
       response = client.post("/add-todo", json=json_request)
       assert response.status_code == 422
    
def test_add_todo_invalid_3() -> None:
     json_request = {"id": 5, "is_done": False}
     with app.test_client() as client:
       response = client.post("/add-todo", json=json_request)
       assert response.status_code == 422
    
def test_add_todo_invalid_4() -> None:
     json_request = {"id": 1,"task": "Go shopping", "is_done": False, "additional_field": "This field is not expected"}
     with app.test_client() as client:
       response = client.post("/add-todo", json=json_request)
       # 201 because pydantic will ignore extra arguments and not raise errors
       assert response.status_code == 201



def test_create_user():
    with app.test_client() as client:
        add_user_json = {"id": 1, "user": "Harry Potter"}
        response = client.post("/add-user", json=add_user_json)

        assert response.status_code == 201
        assert response.json == add_user_json

def test_add_user_invalid_1() -> None:
     with app.test_client() as client:
       response = client.post("/add-user", json="This is not a dictionary")
       assert response.status_code == 422

def test_add_user_invalid_2() -> None:
     json_request = {"id": 4, "task": "Go shopping"}
     with app.test_client() as client:
       response = client.post("/add-user", json=json_request)
       assert response.status_code == 422
    
def test_add_user_invalid_3() -> None:
     json_request = {"id": 5, "user": False}
     with app.test_client() as client:
       response = client.post("/add-user", json=json_request)
       assert response.status_code == 422
    
def test_add_user_invalid_4() -> None:
     json_request = {"id": 1,"user": "Go shopping", "is_done": False, "additional_field": "This field is not expected"}
     with app.test_client() as client:
       response = client.post("/add-user", json=json_request)
       # 201 because pydantic will ignore extra arguments and not raise errors
       assert response.status_code == 201


def test_add_user_invalid_3_unique_id() -> None:
     json_request = {"id": 1, "user": "Jack"}
     with app.test_client() as client:
       response = client.post("/add-user", json=json_request)
       assert response.status_code == 201
     json_request = {"id": 1, "user": "Jack"}
     with app.test_client() as client:
       response = client.post("/add-user", json=json_request)
       assert response.status_code == 422
       