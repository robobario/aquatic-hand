from unittest import TestCase

from actions import Move
from character import Pc
from spacial import Point
from world import World


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        world = World()
        world.arena.getlocation(Point(1, 5)).additem('asdf')
        world.arena.getlocation(Point(0, 5)).additem('item')
        self.assertEqual(world.arena.findcharacter('asdf').gettuple(), Point(1, 5).gettuple())
        world.move('item', 'right', lambda x: x)
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())
        world.move('item', 'up', lambda x: x)
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())

    def test_move_edgecase(self):
        world = World()
        man = Pc()
        world.arena.getlocation(Point(11, 11)).additem(man)
        world.move(man, 'right', lambda x: x)
        self.assertEqual(world.arena.findcharacter(man).gettuple(), Point(11, 11).gettuple())

    def test_death(self):
        world = World()
        man = Pc()
        world.spawn(man)
        location = world.arena.findcharacterlocation(man)
        location.characters[0].kill()
        loc = world.arena.findcharacter(man)
        world.attempt(man, Move('right'))
        self.assertEqual(False, man.alive)
        self.assertEqual(0, len(world.pcs))
        if world.arena.ingrid(loc.add(Point(0, 1))):
            self.assertGreater(len(world.arena.getlocation(loc.add(Point(0, 1))).items), 0)

