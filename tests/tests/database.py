from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from APp.main import app
from APp.config import settings
from APp.database import get_db, Base
from alembic import command
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
    