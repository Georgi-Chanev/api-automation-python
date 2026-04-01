from utils.api_client import APIClient

client = APIClient()

def test_get_users_list():
    response = client.get("/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

def test_single_user():
    response = client.get("/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
