from unittest import TestCase
from arena import Location
from items import Bone

__author__ = 'python'


class TestLocation(TestCase):
    def test_location(self):
        location = Location()
        location.additem('asdf')
        self.assertIn('asdf', location)
        location.removeitem('asdf')
        self.assertNotIn('asdf', location)

    def test_printitem(self):
        location = Location()
        bone = Bone()
        location.additem(bone)
        self.assertEquals(bone, location.getprintitem())

