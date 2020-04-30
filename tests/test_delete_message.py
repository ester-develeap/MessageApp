import pytest

from src.api import app


@pytest.mark.run(order=3)
def test_delete_by_application():
    client = app.test_client()
    url = '/DeleteMessage?applicationId=1'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "2 messages deleted"
    assert response.status_code == 200

    url = '/DeleteMessage?applicationId=15'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "0 messages deleted"
    assert response.status_code == 200

@pytest.mark.run(order=4)
def test_delete_by_session():
    client = app.test_client()
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

@pytest.mark.run(order=5)
def test_delete_by_messagen():
    client = app.test_client()
    url = '/DeleteMessage?messageId=ddd'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "1 messages deleted"
    assert response.status_code == 200

    url = '/DeleteMessage?messageId=hhh'
    response = client.delete(url)
    data=response.get_data().decode()
    assert data == "0 messages deleted"
    assert response.status_code == 200