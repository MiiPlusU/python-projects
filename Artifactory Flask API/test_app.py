import pytest
from app import app
import app as app_module  # so we can monkeypatch app_module.requests

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

class FakeResponse:
    def __init__(self, json_body, status_code=200):
        self._json_body = json_body
        self.status_code = status_code
        self.headers = {"Content-Type": "application/json"}

    def json(self):
        return self._json_body

def test_get_all_artifacts(client, monkeypatch):

    fake_body = {
        "children": [
            {"uri": "/file1.txt"},
            {"uri": "/folder/"},
        ]
    }

    def fake_get(url, headers=None, timeout=None, stream=False):
        return FakeResponse(fake_body, status_code=200)
    
    monkeypatch.setattr(app_module.requests, "get", fake_get)

    response = client.get("/artifacts")

    assert response.status_code == 200

    json_data = response.get_json() 

    expected = [
        {"name": "file1.txt", "uri": "file1.txt"},
        {"name": "folder/", "uri": "folder/"},
    ]

    assert json_data == expected


    

def test_get_failure(client, monkeypatch):

    fake_body = {}


    def fake_get(url, headers=None, timeout=None, stream=False):
        return FakeResponse(fake_body, status_code=500)
    
    monkeypatch.setattr(app_module.requests, "get", fake_get)

    response = client.get(url = '/artifacts')

    assert response.status_code == 500

    assert response.get_json() == {'error': 'failed to read file'}
