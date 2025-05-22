"""
pytests of the REST API app
"""
import os
import pytest
import sys
from server.api.v1.app import create_app


app = create_app()

@pytest.fixture
def client():
    """
    pytest fixture to create a test client for the Flask app
    """
    with app.test_client() as client:
        yield client


def test_not_found(client):
    """
    test the 404 error handler
    """
    response = client.get('/api/v1/non_existent_route')
    assert response.status_code == 404
    assert b'Not Found' in response.data
