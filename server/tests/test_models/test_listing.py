"""
unit tests for listings model
"""
from server.models.listing import Listing
from unittest import TestCase


class TestListing(TestCase):
    """ Tests for the Listing class
    """
    def test_listing(self):
        """ Test that the instance initialises correctly
        """
        listing1 = Listing()
        self.assertEqual(listing1.created_at, listing1.updated_at)
