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
        self.assertCharacterLocation(arena, 1, 2)

    def assertCharacterLocation(self, arena, i, y):
        found = arena.findcharacter('asdf')
        self.assertEqual(found.x, i)
        self.assertEqual(found.y, y)

    def test_moveitem(self):
        arena = Arena(12, 12)
        arena.getlocation(Point(1, 2)).additem('asdf')
        arena.moveitem('asdf', Point(3, 5))
        self.assertCharacterLocation(arena, 3, 5)

    def test_widthAndHeight(self):
        arena = Arena(10, 4)
        self.assertEqual(10, arena.width)
        self.assertEqual(4, arena.height)

    def test_copy(self):
        arena = Arena(12, 12)
        arena.getlocation(Point(1, 2)).additem('asdf')
        copy = arena.copy()
        copy.moveitem('asdf', Point(3, 5))
        self.assertCharacterLocation(copy, 3, 5)
        self.assertCharacterLocation(arena, 1, 2)

    def test_ingrid(self):
        arena = Arena(12, 12)
        self.assertEqual(arena.ingrid(Point(-1, 0)), False)
        self.assertEqual(arena.ingrid(Point(0, -1)), False)
        self.assertEqual(arena.ingrid(Point(1, 0)), True)
        self.assertEqual(arena.ingrid(Point(0, 4)), True)
        self.assertEqual(arena.ingrid(Point(0, 5)), True)
        self.assertEqual(arena.ingrid(Point(1, 12)), False)
        self.assertEqual(arena.ingrid(Point(12, 1)), False)
