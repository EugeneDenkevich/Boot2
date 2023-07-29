from fastapi.testclient import TestClient
from backend.app import create_app

client = TestClient(create_app())

def test_server_online():
    response = client.get("/api-test")
    assert response.status_code == 200