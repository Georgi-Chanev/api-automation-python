from utils.api_client import APIClient

client = APIClient()

def test_status_code():
    response = client.get("/unknown/23")
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "Georgi", "job": "QA Automation"}
    response = client.post("/users", payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Georgi"
