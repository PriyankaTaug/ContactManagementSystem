import pytest
from iterator import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_contact(client):
    response = client.post('/add_contact', json={
        'name': 'John Doe',
        'phone': '1234567890',
        'email': 'john@example.com'
    })
    assert response.status_code == 201
    assert b'Successfully added' in response.data
