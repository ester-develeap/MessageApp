import json

from flask import request

from src.api import app

def test_get_by_application():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 1,
            'message_id': "aaa",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "like"}
    response = client.post(url, data=json.dumps(data))
    data = {'application_id': 1,
            'message_id': "ddd",
            'participants': ["avi", "moshe"],
            'session_id': "xxx",
            'content': "wow"}
    response = client.post(url, data=json.dumps(data))

    url = '/GetMessage?applicationId=1'
    response = client.get(url)
    data=response.get_data()
    data = json.loads(data.decode())
    assert data.__len__() == 5
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

def test_get_by_session():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 1,
            'message_id': "aaa",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "like"}
    response = client.post(url, data=json.dumps(data))
    data = {'application_id': 2,
            'message_id': "bbb",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "ooops"}
    response = client.post(url, data=json.dumps(data))

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

def test_get_by_messagen():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 1,
            'message_id': "aaa",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "like"}
    response = client.post(url, data=json.dumps(data))
    data = {'application_id': 2,
            'message_id': "bbb",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "ooops"}
    response = client.post(url, data=json.dumps(data))

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