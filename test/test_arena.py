from unittest import TestCase

from arena import Arena
from spatial import Point


__author__ = 'python'


class TestArena(TestCase):
    def setUp(self):
        self.arena = Arena(12, 12)

    def test_get_location(self):
        self.arena.get_location(Point(1, 1)).additem('asdf')
        self.arena.get_location(Point(1, 1)).removeitem('asdf')

    def test_find_character(self):
        self.arena.get_location(Point(1, 2)).additem('asdf')
        self.assert_character_location(self.arena, 1, 2)

    def test_move_item(self):
        self.arena.get_location(Point(1, 2)).additem('asdf')
        self.arena.move_item('asdf', Point(3, 5))
        self.assert_character_location(self.arena, 3, 5)

    def test_width_and_height(self):
        arena = Arena(10, 4)
        self.assertEqual(10, arena.width)
        self.assertEqual(4, arena.height)

    def test_copy(self):
        self.arena.get_location(Point(1, 2)).additem('asdf')
        copy = self.arena.copy()
        copy.move_item('asdf', Point(3, 5))
        self.assert_character_location(copy, 3, 5)
        self.assert_character_location(self.arena, 1, 2)

    def test_ingrid(self):
        self.assertEqual(self.arena.in_grid(Point(-1, 0)), False)
        self.assertEqual(self.arena.in_grid(Point(0, -1)), False)
        self.assertEqual(self.arena.in_grid(Point(1, 0)), True)
        self.assertEqual(self.arena.in_grid(Point(0, 4)), True)
        self.assertEqual(self.arena.in_grid(Point(0, 5)), True)
        self.assertEqual(self.arena.in_grid(Point(1, 12)), False)
        self.assertEqual(self.arena.in_grid(Point(12, 1)), False)

    def assert_character_location(self, arena, x, y):
        found = arena.find_character('asdf')
        self.assertEqual(found.x, x)
        self.assertEqual(found.y, y)
