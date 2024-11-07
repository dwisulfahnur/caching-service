import os
import pytest
from sqlmodel import SQLModel, Session, create_engine, delete
from fastapi.testclient import TestClient
from src.main import app
from src.core.database import get_dbsession
from src.models import Payload

# Create a separate database for test using SQLite engine
TEST_DATABASE_URL = "sqlite:///./test_database.db"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={
                            "check_same_thread": False})

# Override the get_session dependency to use the test database


def get_test_dbsession():
    with Session(test_engine) as session:
        yield session


# Apply the override in the FastAPI app
app.dependency_overrides[get_dbsession] = get_test_dbsession


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Create tables in the temporary SQLite database
    SQLModel.metadata.create_all(test_engine)
    yield
    # Teardown: Remove the test database file after the test session
    os.remove("test_database.db")


@pytest.fixture(autouse=True)
def clear_database():
    # Clear data from all tables before each test to ensure a fresh state
    with Session(test_engine) as session:
        session.exec(delete(Payload))  # Truncate the Payload table
        session.commit()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
