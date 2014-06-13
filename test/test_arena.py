from unittest import TestCase

from arena import Arena
from spatial import Point


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
        self.assertEqual(found.x, 1)
        self.assertEqual(found.y, 2)

    def test_moveitem(self):
        arena = Arena(12, 12)
        arena.getlocation(Point(1, 2)).additem('asdf')
        arena.moveitem('asdf', Point(3, 5))
        found = arena.findcharacter('asdf')
        self.assertEqual(found.x, 3)
        self.assertEqual(found.y, 5)

    def test_ingrid(self):
        arena = Arena(12, 12)
        self.assertEqual(arena.ingrid(Point(-1, 0)), False)
        self.assertEqual(arena.ingrid(Point(0, -1)), False)
        self.assertEqual(arena.ingrid(Point(1, 0)), True)
        self.assertEqual(arena.ingrid(Point(0, 4)), True)
        self.assertEqual(arena.ingrid(Point(0, 5)), True)
        self.assertEqual(arena.ingrid(Point(1, 12)), False)
        self.assertEqual(arena.ingrid(Point(12, 1)), False)
