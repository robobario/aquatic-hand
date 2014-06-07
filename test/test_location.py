from unittest import TestCase
from arena import Location

__author__ = 'python'


class TestLocation(TestCase):
    def test_location(self):
        location = Location()
        location.additem('asdf')
        self.assertIn('asdf', location)
        location.removeitem('asdf')
        self.assertNotIn('asdf', location)
