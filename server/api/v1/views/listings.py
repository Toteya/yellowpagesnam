"""
REST API endpoints for listings
"""
from flask import abort, jsonify, request
from server.api.v1.views import app_views
from server.models import storage
from server.models.listing import Listing


@app_views.route('/listings', methods=['GET'], strict_slashes=False)
def get_listings():
    """
    Get all listings
    """
    listings = storage.all(Listing)
    listings = [listing.to_dict() for listing in listings]
    return jsonify(listings), 200

@app_views.route('/listings/<listing_id>', strict_slashes=False)
def get_listing(listing_id):
    """
    Get a specific listing by ID
    """
    listing = storage.get(Listing, listing_id)
    if not listing:
        abort(404, description="Listing not found")
    return jsonify(listing.to_dict()), 200
