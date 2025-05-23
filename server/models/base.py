"""
base/parent model
"""
from datetime import datetime
from mongoengine import Document, StringField, DateTimeField
from uuid import uuid4


class BaseModel(Document):
    """
    Base model class to be inherited by all MongoDB models.
    """
    meta = {'abstract': True}

    id = StringField(primary_key=True, default=lambda: str(uuid4()))
    created_at = DateTimeField()
    updated = DateTimeField()

    def __init__(self, *args, **kwargs):
        """
        Initialize the base model.
        """
        super().__init__(*args, **kwargs)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at 

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if hasattr(self, key):
                    setattr(self, key, value)
    
    def save(self):
        """ Save the object to the database
        """
        self.updated_at = datetime.now()
        # storage.save()
