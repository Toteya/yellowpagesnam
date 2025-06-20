"""
pytests for the REST API `listings` endpoints.
"""
import pytest
from server.models.listing import Listing
from server.models import storage
from test_app import client


@pytest.fixture
def sample_listings():
    """Fixture to create a sample listing."""
    listing1 = Listing(name="Test Listing", category="Test Category")
    listing1.save()
    listing2 = Listing(id='5fbb6d0a-cd33', name="Another Listing", category="Another Category")
    listing2.save()
    yield [listing1, listing2]
    storage.delete(listing1)
    storage.delete(listing2)

def test_get_listings(client, sample_listings):
    """Test retrieving all listings."""
    response = client.get('/api/v1/listings')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    for listing in sample_listings:
        assert any(item["id"] == listing.id for item in data)

def test_get_listing_success(client, sample_listings):
    """Test retrieving a specific listing by ID."""
    listing = sample_listings[0]
    response = client.get(f'/api/v1/listings/{listing.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == listing.id
    assert data["name"] == listing.name

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
        "phone_numbers": ["1234567890", "0987654321"]
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

def test_delete_listing(client, sample_listings):
    """Test deleting a listing."""
    listing = sample_listings[0]
    response = client.delete(f'/api/v1/listings/{listing.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['Deleted'] == f'Listing {listing.name}'

    # Verify deletion
    deleted_listing = storage.get(Listing, listing.id)
    assert deleted_listing is None

    # Attempt to delete a non-existent listing
    response = client.delete('/api/v1/listings/nonexistent-id')
    assert response.status_code == 404
    assert b'Listing not found' in response.data


def test_add_media_success(client, sample_listings, monkeypatch):
    """Test adding media to a listing."""
    listing = sample_listings[0]

    # Mock environment variables and file system interactions
    media_dir = "/mock/media"
    monkeypatch.setenv("DIRECTORY_MEDIA_DIRPATH", media_dir)

    def mock_exists(path):
        valid_paths = [media_dir, f"{media_dir}/all/test_image.jpg"]
        return path in valid_paths

    def mock_copy(src, dst):
        pass  # Simulate file copying without actual filesystem operations

    monkeypatch.setattr("os.path.exists", mock_exists)
    monkeypatch.setattr("shutil.copy", mock_copy)
    monkeypatch.setattr("os.makedirs", lambda path: None)

    # Mock file in media directory
    filename = "test_image.jpg"

    # Add media to listing
    response = client.post(
        f"/api/v1/listings/{listing.id}/photos",
        json={"filename": filename},
    )
    assert response.status_code == 200
    data = response.get_json()
    assert any(photo.endswith(filename) for photo in data["photos"])

def test_add_media_invalid_format(client, sample_listings):
    """Test adding media with invalid format."""
    listing = sample_listings[0]
    response = client.post(
        f"/api/v1/listings/{listing.id}/photos",
        json={"filename": "invalid_file.txt"},
    )
    assert response.status_code == 400
    assert b"Invalid file format" in response.data

def test_add_media_missing_file(client, sample_listings):
    """Test adding media with missing filename."""
    listing = sample_listings[0]
    response = client.post(f"/api/v1/listings/{listing.id}/photos", json={})
    assert response.status_code == 400
    assert b"Missing filename" in response.data

def test_add_media_nonexistent_listing(client):
    """Test adding media to a non-existent listing."""
    response = client.post(
        "/api/v1/listings/nonexistent-id/photos",
        json={"filename": "test_image.jpg"},
    )
    assert response.status_code == 404
    assert b"Listing not found" in response.data

def test_add_media_file_not_found(client, sample_listings, monkeypatch):
    """Test adding media when the file is not found in the media folder."""
    # Arrange
    listing = sample_listings[0]

    # Mock environment variables and file system interactions
    media_dir = "/mock/media"  # Fake media directory path
    monkeypatch.setenv("DIRECTORY_MEDIA_DIRPATH", media_dir)

    def mock_exists(path):
        # Simulate that the media directory exists but the file does not
        return path == media_dir

    monkeypatch.setattr("os.path.exists", mock_exists)

    # Act
    response = client.post(
        f"/api/v1/listings/{listing.id}/photos",
        json={"filename": "missing_file.jpg"},  # Provide a filename that doesn't exist
    )

    # Assert
    assert response.status_code == 404  # Expect not found response
    assert b"File not found" in response.data  # Verify error message

