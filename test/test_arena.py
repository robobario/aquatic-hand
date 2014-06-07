from unittest import TestCase
from arena import Arena
from spacial import Point

__author__ = 'python'


class TestArena(TestCase):
    def test_getlocation(self):
        arena = Arena(12, 12)
        arena.getlocation(Point(1, 1)).additem('asdf')
        arena.getlocation(Point(1, 1)).removeitem('asdf')

    def test_findcharacter(self):
        arena = Arena(12, 12)
        arena.getlocation(Point(1, 2)).additem('asdf')
        found = arena.findcharacter('asdf')
        print(found.x)
        print(found.y)

