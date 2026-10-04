import pytest
from jose import jwt 
from APp import schemas
from .database import client,Session
from APp.config import settings
@pytest.fixture
def test_user(session):
    user_data = {"email": "hello123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user




def test_root(client, Session):
    res = client.get(client)
    print(res.json().get('message'))
    assert (res.json().get('message')) == 'Hello World'

def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
    
def test_login_user(client, test_user):
    res = client.post("/login", data={"username":  test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

def test_incorrect_login(test_user, client):
    res = client.post("/login", data={"username": test_user['email'], "password": "wrongPassword"})
    
    
    assert res.status_code == 403
    assert res.json().get('detail') == 'Invalid Credentials'

