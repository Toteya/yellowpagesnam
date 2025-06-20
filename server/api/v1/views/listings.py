"""
REST API endpoints for listings
"""
from flask import abort, jsonify, request
from mongoengine.errors import FieldDoesNotExist
from server.api.v1.views import app_views
from server.models import storage
from server.models.listing import Listing



@app_views.route('/listings', methods=['GET'], strict_slashes=False)
def get_listings():
    """ Get all listings
    """
    listings = storage.all(Listing)
    listings = sorted(listings, key=lambda x: x.name)
    listings = [listing.to_dict() for listing in listings]
    return jsonify(listings), 200

@app_views.route('/listings/<listing_id>', strict_slashes=False)
def get_listing(listing_id):
    """ Get a specific listing by ID
    """
    listing = storage.get(Listing, listing_id)
    if not listing:
        abort(404, description="Listing not found")
    return jsonify(listing.to_dict()), 200

@app_views.route('/listings', methods=['POST'], strict_slashes=False)
def create_listing():
    """ Create a new directory listing
    """
    data = request.get_json(silent=True)
    if data is None:
        abort(400, description="Not a JSON")
    
    required_fields = ['name', 'category']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing {field}")

    try:
        listing = Listing(**data)
    except FieldDoesNotExist as e:
        print(f"FieldDoesNotExist Exception: {e}")
        abort(400, description=f"Invalid field: {e}")
    listing.save()
    return jsonify(listing.to_dict()), 201

@app_views.route('/listings/<listing_id>', methods=['DELETE'], strict_slashes=False)
def delete_listing(listing_id):
    """ Delete a directory listing
    """
    listing = storage.get(Listing, listing_id)
    if not listing:
        abort(404, description="Listing not found")

    storage.delete(listing)
    return jsonify({'Deleted': f'Listing {listing.name}'}), 200

@app_views.route('/listings/<listing_id>/photos', methods=['POST'], strict_slashes=False)
def add_media(listing_id):
    """ Add a photo to the listing
    """
    listing = storage.get(Listing, listing_id)
    if not listing:
        abort(404, description='Listing not found')
    
    data = request.get_json(silent=True)
    if data is None:
        abort(400, description='Not a JSON')
    filename = data.get('filename')
    if not filename:
        abort(400, description='Missing filename')
    try:
        listing.add_media(filename)
    except FileNotFoundError as e:
        abort(404, description='File not found')
    except ValueError:
        abort(400, description='Invalid file format')
    # Add a logger to log the either internal errors (e.g. EnvironmentError)

    listing.save()
    return jsonify(listing.to_dict()), 200
