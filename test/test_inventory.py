from unittest import TestCase

import arena
import character
import queries
import spatial
import world


__author__ = 'python'


class TestInventory(TestCase):
    def test_inventory(self):
        an_arena = arena.Arena(12, 12)
        snap = world.WorldSnapshot(an_arena)
        test_loc = an_arena.get_location(spatial.Point(1, 1))
        test_pc = character.Pc()
        test_loc.additem(test_pc)
        self.assertEquals(test_pc.inventory, queries.inventory(snap, test_pc.id))