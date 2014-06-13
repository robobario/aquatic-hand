from unittest import TestCase

import actions
import bestiary
import character
import items
import spatial
import world


__author__ = 'python'


class TestWorld(TestCase):
    def test_move(self):
        the_world = world.World()
        man = character.Pc()
        the_world.current.arena.getlocation(spatial.Point(1, 5)).additem(man)
        self.assertEqual(the_world.current.arena.findcharacter(man).gettuple(), spatial.Point(1, 5).gettuple())
        world.move(the_world.current, man, 'E', lambda x: x)
        self.assertEqual(the_world.current.arena.findcharacter(man).gettuple(), spatial.Point(1, 6).gettuple())
        world.move(the_world.current, man, 'N', lambda x: x)
        self.assertEqual(the_world.current.arena.findcharacter(man).gettuple(), spatial.Point(0, 6).gettuple())

    def test_move_edgecase(self):
        the_world = world.World()
        man = character.Pc()
        the_world.current.arena.getlocation(spatial.Point(11, 11)).additem(man)
        world.move(the_world.current, man, 'E', lambda x: x)
        self.assertEqual(the_world.current.arena.findcharacter(man).gettuple(), spatial.Point(11, 11).gettuple())

    def test_death(self):
        the_world = world.World()
        man = character.Pc()
        world.spawn(the_world.current, man)
        location = the_world.current.arena.findcharacterlocation(man)
        location.characters[0].kill()
        loc = the_world.current.arena.findcharacter(man)
        the_world.attempt(man, actions.Move('E'))
        self.assertEqual(False, man.alive)
        self.assertEqual(0, len(the_world.current.pcs))
        if the_world.current.arena.ingrid(loc.add(spatial.Point(0, 1))):
            self.assertGreater(len(the_world.current.arena.getlocation(loc.add(spatial.Point(0, 1))).items), 0)

    def test_pickup(self):
        the_world = world.World()
        man = character.Pc()
        key = items.Bone()
        the_world.current.arena.getlocation(spatial.Point(5, 5)).additem(man)
        the_world.current.arena.getlocation(spatial.Point(5, 5)).items.append(key)
        world.pickup(the_world.current, man, lambda x: x)
        self.assertGreater(len(man.inventory), 0)
        kitty = bestiary.Cat()
        the_world.current.arena.getlocation(spatial.Point(5, 7)).additem(kitty)
        kitty.kill()
        the_world.attempt(man, actions.Move('E'))
        the_world.attempt(man, actions.Move('E'))
        world.pickup(the_world.current, man, lambda x: x)



