import json

from flask import request

from src.api import app

def test_delete_by_application():
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

    url = '/DeleteMessage?applicationId=5'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "2 messages deleted"
    assert response.status_code == 200

    url = '/DeleteMessage?applicationId=15'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "0 messages deleted"
    assert response.status_code == 200


def test_delete_by_session():
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
            'session_id': "xxx",
            'content': "ooops"}
    response = client.post(url, data=json.dumps(data))

    url = '/DeleteMessage?sessionId=www'
    response = client.delete(url)
    data = response.get_data().decode()
    assert data == "1 messages deleted"
    assert response.status_code == 200

    url = '/DeleteMessage?sessionId=qqq'
    response = client.delete(url)
    data = response.get_data().decode()
    assert data == "0 messages deleted"
    assert response.status_code == 200

def test_delete_by_messagen():
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

    url = '/DeleteMessage?messageId=bbb'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "1 messages deleted"
    assert response.status_code == 200

    url = '/DeleteMessage?messageId=hhh'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "0 messages deleted"
    assert response.status_code == 200