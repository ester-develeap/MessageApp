import json

import pytest

from src.api import app

@pytest.mark.run(order=2)
def test_get_by_application():
    client = app.test_client()
    url = '/GetMessage?applicationId=1'
    response = client.get(url)
    data=response.get_data()
    data = json.loads(data.decode())
    assert data.__len__() == 2
    assert response.status_code == 200

    url = '/GetMessage?applicationId="sss"'
    response = client.get(url)
    data=response.get_data()
    assert data == b'arguments not correct'
    assert response.status_code == 400

    url = '/GetMessage?applicationId=17'
    response = client.get(url)
    data=response.get_data()
    data = json.loads(data.decode())
    assert data.__len__() == 0
    assert response.status_code == 200



@pytest.mark.run(order=2)
def test_get_by_session():
    client = app.test_client()
    url = '/GetMessage?sessionId=www'
    response = client.get(url)
    data=response.get_data()
    data = json.loads(data.decode())
    assert data.__len__() == 2
    assert response.status_code == 200

    url = '/GetMessage?sessionId=3'
    response = client.get(url)
    data=response.get_data()
    data = json.loads(data.decode())
    assert data.__len__() == 0
    assert response.status_code == 200

@pytest.mark.run(order=2)
def test_get_by_message():
    client = app.test_client()
    url = '/GetMessage?messageId=aaa'
    response = client.get(url)
    data = response.get_data()
    data = json.loads(data.decode())
    assert data["message_id"] == "aaa"
    assert response.status_code == 200

    url = '/GetMessage?messageId=5'
    response = client.get(url)
    data = response.get_data()
    data = json.loads(data.decode())
    assert data == {}
    assert response.status_code == 200