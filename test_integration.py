import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c

def test_home(client):
    rv = client.get('/')
    assert rv.data == b"Hello from Python App!"
