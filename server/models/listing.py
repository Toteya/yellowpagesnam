"""
Directory listing implementation
"""
from mongoengine import DictField, EmailField, IntField, ListField, PointField, StringField
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
            'likes',
            'reviews'
        ]
    }

    name = StringField(max_length=255, required=True)
    category = StringField(max_length=255, required=True)
    email = EmailField(max_length=255, required=False)
    website = StringField(max_length=255, required=False)
    location = PointField(required=False)  # GeoJSON point for location
    phone_numbers = ListField(StringField(max_length=60), required=False)
    photos = ListField(StringField(max_length=255), required=False)
    likes = IntField(default=0, required=False)
    reviews = ListField(DictField(), default=list, required=False)

    def add_photo(self, filename):
        """ Adds a photo to the listing
        """
        dirpath = 'photos'
        filepath = f'{dirpath}/{self.id}/{filename}'
        self.photos.append(filepath)
