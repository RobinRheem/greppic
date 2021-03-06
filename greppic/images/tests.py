from starlette.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_list():
    response = client.get('/api/v1/images')
    assert response.status_code == 200
    assert response.json() == 'Image List'
