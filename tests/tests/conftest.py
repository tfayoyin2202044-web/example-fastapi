from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from APp.main import app
from APp.config import settings
from APp.database import get_db, Base
from alembic import command
from APp.oauth2 import create_access_token
from APp import models

#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



app.dependency_overrides[get_db] = override_get_db



client = TestClient(app)

@pytest.fixture(scope="function")
def Session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try: 
        yield db
    finally:
        db.close()



@pytest.fixture()
def client(Session):
    db = override_get_db()
    
    try: 
        yield Session
    finally:
        db.close(Session.close)
    app.dependency_overrides[get_db] = override_get_db    
    yield TestClient(app)
    

@pytest.fixture
def test_user(session):
    user_data = {"email": "hello123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, Session):
    posts_data = []
