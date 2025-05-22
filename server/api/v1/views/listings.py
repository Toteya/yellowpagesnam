"""
REST API endpoints for listings
"""
from flask import abort, jsonify, request
from server.api.v1.views import app_views


@app_views.route('/listings', methods=['GET'], strict_slashes=False)
def get_listings():
    """
    Get all listings
    """
    listings = []
    return jsonify(listings), 200
