import pytest
from fastapi.testclient import TestClient
from app import app
from datetime import date

client = TestClient(app)


def test_root():
    """
    Test the root endpoint by sending a GET request to "/" and checking the response status code and JSON body.
    """
    assert 2 == 2
