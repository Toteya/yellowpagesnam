"""
Directory listing implementation
"""
from mongoengine import StringField, EmailField, URLField
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
            'phone_number1',
            'phone_number2'
        ]
    }

    name = StringField(max_length=255, required=True)
    category = StringField(max_length=255, required=True)
    email = EmailField(max_length=255, required=False)
    website = URLField(max_length=255, required=False)
    phone_number1 = StringField(max_length=60, required=False)
    phone_number2 = StringField(max_length=60, required=False)
