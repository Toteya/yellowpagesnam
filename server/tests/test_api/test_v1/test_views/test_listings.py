"""
pytests for the REST API `listings` endpoints.
"""
import pytest
from server.models.listing import Listing
from server.models import storage
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
    assert b'Listing not found' in response.data

def test_create_listing(client):
    """Test creating a new listing."""
    # Valid data
    valid_data = {
        "name": "Test Listing",
        "category": "Test Category",
        "email": "test@example.com",
        "website": "https://example.com",
        "phone_number1": "1234567890",
        "phone_number2": "0987654321"
    }
    response = client.post('/api/v1/listings', json=valid_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == valid_data["name"]
    assert data["category"] == valid_data["category"]
    assert "id" in data  # Ensure ID is generated

    listing_id = data["id"]
    saved_listing = storage.get(Listing, listing_id)
    assert saved_listing is not None
    assert saved_listing.name == data["name"]
    assert saved_listing.category == data["category"]

    # Missing required field
    invalid_data = {"name": "Missing Category"}
    response = client.post('/api/v1/listings', json=invalid_data)
    assert response.status_code == 400
    assert b"Missing category" in response.data

    # Invalid JSON
    response = client.post('/api/v1/listings', data="Not a JSON")
    assert response.status_code == 400
    assert b"Not a JSON" in response.data
