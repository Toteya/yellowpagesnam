"""
Directory listing implementation
"""
from mongoengine import StringField, EmailField, ListField, PointField
from server.models.base import BaseModel


class Listing(BaseModel):
    """
    Directory listing model.
    """
    meta = {
        'collection': 'listings',
        'indexes': [
            'name',
            'category',
            'email',
            'website',
            'location',
            'phone_numbers',
        ]
    }

    name = StringField(max_length=255, required=True)
    category = StringField(max_length=255, required=True)
    email = EmailField(max_length=255, required=False)
    website = StringField(max_length=255, required=False)
    location = PointField(required=False)  # GeoJSON point for location
    phone_numbers = ListField(StringField(max_length=60), required=False)
