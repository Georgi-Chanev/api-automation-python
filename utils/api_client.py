import requests

class APIClient:
    BASE_URL = "https://reqres.in/api"

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}")

    def post(self, endpoint, data=None):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=data)
