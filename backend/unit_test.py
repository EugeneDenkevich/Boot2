from fastapi.testclient import TestClient
# from src.api.create_app import app
from src.api.crud import *


client = TestClient(app)


def test_server_is_on():
    response = client.get("/api/test")
    assert response.status_code == 200
