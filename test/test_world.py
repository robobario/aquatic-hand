from unittest import TestCase
from npc import Npc

from pc import Pc

from spacial import Point

from world import World


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        world = World()
        world.arena.getlocation(Point(1, 5)).additem('asdf')
        world.arena.getlocation(Point(0, 5)).additem('item')
        world.move('item', 'right')
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())
        world.move('item', 'up')
        self.assertEqual(world.arena.findcharacter('item').gettuple(), Point(0, 6).gettuple())

    def test_moveattack(self):
        world = World()
        man = Pc()
        world.spawn(man)
        cat = Npc('kitty')
        world.arena.getlocation(Point(0, 1)).additem(cat)
        cathp = world.arena.getlocation(Point(0, 1)).characters[0].hp
        expected = 100
        self.assertEqual(cathp, expected)
        world.move(man, 'right')
        self.assertEqual(world.arena.findcharacter(man).gettuple(), (0, 0))
        cathp = world.arena.getlocation(Point(0, 1)).characters[0].hp
        expected = 90
        self.assertEqual(cathp, expected)
