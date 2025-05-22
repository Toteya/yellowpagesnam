"""
base model unit tests
"""
from unittest import TestCase
from server.models.base import BaseModel


class Test_Base(TestCase):
    """ Test the Base Model
    """
    def test_base(self):
        """ Test the Base Model
        """
        b1 = BaseModel()
        self.assertTrue(isinstance(b1, BaseModel))
