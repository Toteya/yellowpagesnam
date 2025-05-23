"""
base/parent model
"""
from datetime import datetime, timezone
from mongoengine import Document, StringField, DateTimeField
from uuid import uuid4


class BaseModel(Document):
    """
    Base model class to be inherited by all MongoDB models.
    """
    meta = {'abstract': True}

    id = StringField(primary_key=True, default=lambda: str(uuid4()))
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField()


    def save(self, *args, **kwargs):
        """ Save the object to the database
        """
        if not self.updated_at:
            self.updated_at = self.created_at
        else:
            self.updated_at = datetime.now(timezone.utc)
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if hasattr(self, key):
                    setattr(self, key, value)
    
        return super().save(*args, **kwargs)
