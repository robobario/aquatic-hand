from unittest import TestCase

from character import Character
from spacial import Point
from world import World


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        world = World()
        world.arena.getlocation(Point(1, 5)).additem('asdf')
        world.arena.getlocation(Point(0, 5)).additem('item')
        world.move('asdf', 'up')
        self.assertEqual(world.arena.findcharacter('asdf').gettuple(), Point(1, 5).gettuple())
        world.move('item', 'right')
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())
        world.move('item', 'up')
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())

    def test_spawnMobsOnAttempt(self):
        world = World()
        world.genMobs = lambda heroes: [Character()]
        world.rng = lambda: 3
        world.spawnMobs()
        location = world.arena.getlocation(Point(3, 3))
        self.assertEqual(1, len(location.characters))



