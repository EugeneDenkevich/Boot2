from fastapi.testclient import TestClient
from src.api.create_app import app


client = TestClient(app)


def test_valid_id():
    response = client.get("/api/test")
    assert response.status_code == 200
