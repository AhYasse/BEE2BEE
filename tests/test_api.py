
import pytest
from fastapi.testclient import TestClient
from bee2bee.api import app

@pytest.fixture
def client():
    # We use TestClient which makes requests to the app.
    # Note: bee2bee.api.node will be None unless lifespan is called, 
    # but TestClient handles lifespan in newer versions or we can force it.
    with TestClient(app) as c:
        yield c

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "node_id" in response.json()

def test_get_peers(client):
    response = client.get("/peers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_providers(client):
    response = client.get("/providers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
