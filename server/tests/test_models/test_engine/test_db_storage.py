"""
unit tests for Mongo DB storage engine
"""
from unittest import TestCase
from server.models import storage
from server.models.listing import Listing

class TestDBStorage(TestCase):
    """ Tests the database storage engine DBStorage
    """
    @classmethod
    def setUpClass(cls):
        """ Set up the test class
        """
        storage.clear()

    def test_db_storage(self):
        """ Test that the storage engine initialises
        """
        listing1 = Listing(
            name="Listing 1",
            category="Test Category",
            email="test@mail.com",
            website="http://test.com"
        )
        listing2 = Listing(
            name="Listing 2",
            category="Test Category 2",
            email="test2@mail.com",
            website="http://test2.com"
        )
        listing1.save()
        listing2.save()

        listings = storage.all(Listing)
        self.assertEqual(len(listings), 2)
        self.assertTrue('Listing 1' in [listing['name'] for listing in listings])
