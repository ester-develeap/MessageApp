from flask import Flask
import json

from src.api import app

def test_health():
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.get_data() == b'hello'
    assert response.status_code == 200
