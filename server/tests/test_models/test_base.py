"""
base model unit tests
"""
import unittest
from server.models.base import BaseModel
from server.models.listing import Listing


class Test_Base(unittest.TestCase):
    """ Test the Base Model
    """
    def test_base(self):
        """ Test the Base Model
        """
        b1 = BaseModel()
        self.assertTrue(isinstance(b1, BaseModel))

    def test_to_dict(self):
        """ Test the to_dict method
        """
        listing1 = Listing(name="my_listing", category="my_category")
        listing1.save()

        expected_dict_subset = {'name': 'my_listing', '__class__': 'Listing'}
        
        for key, value in expected_dict_subset.items():
            self.assertIn(key, listing1.to_dict())
            self.assertEqual(listing1.to_dict().get(key), value)
    
    def test_save(self):
        """ Test the save method
        """
        listing1 = Listing(name="my_listing", category="my_category")
        listing1.save()
        self.assertEqual(listing1.created_at, listing1.updated_at)
        
        # Update the listing
        listing1.name = "updated_listing"
        listing1.save()
        
        # Check that updated_at is different from created_at
        self.assertNotEqual(listing1.created_at, listing1.updated_at)
