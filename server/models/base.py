"""
base/parent model
"""
from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.orm import DeclarativeBase
from uuid import uuid4


class Base(DeclarativeBase):
    pass


class BaseModel():
    """
    Base model class to be inherited by all models.
    """
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(String(26), nullable=False)
    updated_at = Column(String(26), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initialize the base model.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at 

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if hasattr(self, key):
                    setattr(self, key, value)
