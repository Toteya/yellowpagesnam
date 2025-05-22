"""
Directory listing implementation
"""
from sqlalchemy import Column, ForeignKey, String
from server.models.base import Base, BaseModel


class Listing(BaseModel, Base):
    """
    Directory listing model.
    """
    __tablename__ = 'listings'

    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    phone_number1 = Column(String(60), nullable=True)
    phone_number2 = Column(String(60), nullable=True)
