from unittest import TestCase

from arena import Arena
from bestiary import Cat
from game import Snapshot
from pc import Pc
from snapshot_printer import snapshotToString
from spacial import Point
from world import WorldSnapshot


__author__ = 'python'


class TestSnapshotToString(TestCase):
    def test_snapshotToString(self):
        snapshot = Snapshot(WorldSnapshot(Arena(1,1)), Pc())
        stringed = snapshotToString(snapshot)
        expected = "###\n# #\n###\nHP: 100, Strength: 10"
        self.assertEqual(expected,stringed)

    def test_snapshotWithDude(self):
        arena = Arena(1, 1)
        location = arena.getlocation(Point(0,0))
        man = Pc()
        location.additem(man)
        snapshot = Snapshot(WorldSnapshot(arena), man)
        stringed = snapshotToString(snapshot)
        expected = "###\n#\u263A#\n###\nHP: 100, Strength: 10"
        self.assertEqual(expected,stringed)

    def test_snapshotWithCat(self):
        arena = Arena(1, 1)
        location = arena.getlocation(Point(0, 0))
        cat = Cat()
        location.additem(cat)
        snapshot = Snapshot(WorldSnapshot(arena), cat)
        stringed = snapshotToString(snapshot)
        expected = "###\n#x#\n###\nHP: 10, Strength: 2"
        self.assertEqual(expected, stringed)

    def test_emptyArena(self):
        snapshot = Snapshot(WorldSnapshot(Arena(0,0)), Pc())
        self.assertRaises(Exception, lambda: snapshotToString(snapshot))

    def test_snapshotNone(self):
        self.assertRaises(Exception, lambda: snapshotToString(None))