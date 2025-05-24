"""
pytests for the REST API `listings` endpoints.
"""
import pytest
from server.models.listing import Listing
from test_app import client


@pytest.fixture
def sample_listing():
    """Fixture to create a sample listing."""
    listing = Listing(name="Test Listing", category="Test Category")
    listing.save()
    return listing

def test_get_listings(client, sample_listing):
    """Test retrieving all listings."""
    response = client.get('/api/v1/listings')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(item["id"] == sample_listing.id for item in data)

def test_get_listing_success(client, sample_listing):
    """Test retrieving a specific listing by ID."""
    response = client.get(f'/api/v1/listings/{sample_listing.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == sample_listing.id
    assert data["name"] == sample_listing.name

def test_get_listing_not_found(client):
    """Test retrieving a non-existent listing."""
    response = client.get('/api/v1/listings/nonexistent-id')
    assert response.status_code == 404
    print('RAW RESPONSE DATA: ', response.data.decode())
    assert b'Listing not found' in response.data
