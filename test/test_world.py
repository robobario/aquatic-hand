from unittest import TestCase

from spacial import Point

from world import World


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        world = World()
        world.arena.getlocation(Point(1, 5)).additem('asdf')
        world.move('asdf', 'up')
        world.arena.findcharacter('asdf')