
from fastapi.testclient import TestClient
from UsersService import app

client = TestClient(app)

def test_get_users():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == "Allow users: id-1:User1; id-2:User2; id-3:User3"

def test_get_cancel_users():
    response = client.get('/cancel_users')
    assert response.status_code == 200
    assert response.json() == "Cancel users: id-4:User4; id-5:User5; id-6:User6"