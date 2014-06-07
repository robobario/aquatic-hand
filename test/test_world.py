from unittest import TestCase

from spacial import Point

from world import World


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        world = World()
        world.arena.getlocation(Point(1, 5)).additem('asdf')
        world.arena.getlocation(Point(0, 5)).additem('item')
        world.move('asdf', 'up', lambda x: x)
        self.assertEqual(world.arena.findcharacter('asdf').gettuple(), Point(1, 5).gettuple())
        world.move('item', 'right', lambda x: x)
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())
        world.move('item', 'up', lambda x: x)
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())

    def test_death(self):
        world = World()
        man = Pc()
        world.spawn(man)
        location = world.arena.findcharacterlocation(man)
        location.characters[0].kill()
        loc = world.arena.findcharacter(man).gettuple()
        newloc = loc[0], loc[1] + 1
        world.attempt(man, Move('right'))
        self.assertEqual(world.arena.findcharacter(man).gettuple(), newloc)
        self.assertEqual(False, man.alive)
