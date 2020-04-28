import json
from src.api import app

def test_post_succes():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': "www",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'the message was added succesfully'
    assert response.status_code == 200

def test_post_exist():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': "www",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'message_id is alredy exist'
    assert response.status_code == 400

#applicationId
def test_post_applicationId_not_number():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': "5",
            'session_id': "www",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'application_id must be number'
    assert response.status_code == 400

def test_post_applicationId_empty():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': "",
            'session_id': "www",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'application_id cannot be empty'
    assert response.status_code == 400

def test_post_no_applicationId():
    client = app.test_client()
    url = '/AddMessage'
    data = {'session_id': "www",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'data not correct'
    assert response.status_code == 400

