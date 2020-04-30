import json
import pytest

from src.api import app

@pytest.mark.run(order=1)
def test_post_succes():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 3,
            'message_id': "aaa",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "hello world"}
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'the message was added succesfully'
    assert response.status_code == 200

    url = '/AddMessage'
    data = {'application_id': 1,
            'message_id': "bbb",
            'participants': ["avi", "moshe"],
            'session_id': "www",
            'content': "hello world"}
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'the message was added succesfully'
    assert response.status_code == 200

    url = '/AddMessage'
    data = {'application_id': 1,
            'message_id': "ccc",
            'participants': ["avi", "moshe"],
            'session_id': "xxx",
            'content': "hello world"}
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'the message was added succesfully'
    assert response.status_code == 200

    url = '/AddMessage'
    data = {'application_id': 2,
            'message_id': "ddd",
            'participants': ["avi", "moshe"],
            'session_id': "zzz",
            'content': "hello world"}
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'the message was added succesfully'
    assert response.status_code == 200

@pytest.mark.run(order=2)
def test_post_exist():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': "www",
            'message_id': "ddd",
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

#sessionId
def test_post_sessionId_not_number():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': 12,
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'session_id must be string'
    assert response.status_code == 400

def test_post_sessionId_empty():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id':3,
            'session_id': "",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'session_id cannot be empty'
    assert response.status_code == 400

def test_post_no_sessionId():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id':3,
            'ssssiss_id': "www",
            'message_id': "sss",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'data not correct'
    assert response.status_code == 400

#messageId
def test_post_messageId_not_number():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': "ddd",
            'message_id': 12,
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'message_id must be string'
    assert response.status_code == 400

def test_post_messageId_empty():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 3,
            'session_id': "sss",
            'message_id': "",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'message_id cannot be empty'
    assert response.status_code == 400

def test_post_no_messageId():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id':3,
            'sessionId': "www",
            'participants': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'data not correct'
    assert response.status_code == 400

#participants
def test_post_participants_not_list():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': "ddd",
            'message_id': "ff",
            'participants': "avi,moshe",
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'participants must be list'
    assert response.status_code == 400

def test_post_participants_empty():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id':3,
            'session_id': "sss",
            'message_id': "rrr",
            'participants': [],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'participants cannot be empty'
    assert response.status_code == 400

def test_post_no_participants():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id':3,
            'message_id': "rrr",
            'sessionId': "www",
            'par': ["avi", "moshe"],
            'content': "hello world"}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'data not correct'
    assert response.status_code == 400

#content
def test_post_content_not_number():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id': 5,
            'session_id': "ddd",
            'message_id': "12",
            'participants': ["avi", "moshe"],
            'content': [12]}
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'content must be string'
    assert response.status_code == 400

def test_post_no_content():
    client = app.test_client()
    url = '/AddMessage'
    data = {'application_id':3,
            'sessionId': "www",
            'participants': ["avi", "moshe"],
            }
    x = client.post(url, data=json.dumps(data))
    response = client.post(url, data=json.dumps(data))
    assert response.get_data() == b'data not correct'
    assert response.status_code == 400