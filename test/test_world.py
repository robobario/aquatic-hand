from unittest import TestCase

from actions import Move
from bestiary import Cat
from character import Pc
from items import Bone
from spatial import Point
from world import World, move, pickup


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        world = World()
        man = Pc()
        world.current.arena.getlocation(Point(1, 5)).additem(man)
        self.assertEqual(world.current.arena.findcharacter(man).gettuple(), Point(1, 5).gettuple())
        move(world.current, man, 'E', lambda x: x)
        self.assertEqual(world.current.arena.findcharacter(man).gettuple(), Point(1, 6).gettuple())
        move(world.current, man, 'N', lambda x: x)
        self.assertEqual(world.current.arena.findcharacter(man).gettuple(), Point(0, 6).gettuple())

    def test_move_edgecase(self):
        world = World()
        man = Pc()
        world.current.arena.getlocation(Point(11, 11)).additem(man)
        move(world.current, man, 'E', lambda x: x)
        self.assertEqual(world.current.arena.findcharacter(man).gettuple(), Point(11, 11).gettuple())

    def test_death(self):
        world = World()
        man = Pc()
        world.spawn(world.current, man)
        location = world.current.arena.findcharacterlocation(man)
        location.characters[0].kill()
        loc = world.current.arena.findcharacter(man)
        world.attempt(world.current, man, Move('E'))
        self.assertEqual(False, man.alive)
        self.assertEqual(0, len(world.current.pcs))
        if world.current.arena.ingrid(loc.add(Point(0, 1))):
            self.assertGreater(len(world.current.arena.getlocation(loc.add(Point(0, 1))).items), 0)

    def test_pickup(self):
        world = World()
        man = Pc()
        key = Bone()
        world.current.arena.getlocation(Point(5, 5)).additem(man)
        world.current.arena.getlocation(Point(5, 5)).items.append(key)
        pickup(world.current, man, lambda x: x)
        self.assertGreater(len(man.inventory), 0)
        kitty = Cat()
        world.current.arena.getlocation(Point(5, 7)).additem(kitty)
        kitty.kill()
        world.attempt(world.current, man, Move('E'))
        world.attempt(world.current, man, Move('E'))
        pickup(world.current, man, lambda x: x)



