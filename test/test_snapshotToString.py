from unittest import TestCase

from arena import Arena
from bestiary import Cat
from character import Pc
from game import Snapshot
from snapshot_printer import snapshot_to_string
from spatial import Point
from world import WorldSnapshot


__author__ = 'python'


class TestSnapshotToString(TestCase):
    def test_snapshot_with_dude(self):
        pc = Pc()
        arena = Arena(1, 1)
        arena.get_location(Point(0, 0)).additem(pc)
        snapshot = Snapshot(WorldSnapshot(arena), pc.id, [])
        stringed = snapshot_to_string(snapshot)
        expected = "###\n#\u263A#\n###\nHP: 100, Strength: 10"
        self.assertEqual(expected, stringed)

    def test_snapshot_with_cat(self):
        arena = Arena(1, 1)
        location = arena.get_location(Point(0, 0))
        cat = Cat()
        location.additem(cat)
        snapshot = Snapshot(WorldSnapshot(arena), cat.id, [])
        stringed = snapshot_to_string(snapshot)
        expected = "###\n#x#\n###\nHP: 10, Strength: 2"
        self.assertEqual(expected, stringed)

    def test_snapshot_with_log(self):
        arena = Arena(1, 1)
        location = arena.get_location(Point(0, 0))
        cat = Cat()
        location.additem(cat)
        log = ["loglog", "log2"]
        snapshot = Snapshot(WorldSnapshot(arena), cat.id, log)
        stringed = snapshot_to_string(snapshot)
        expected = "###\n#x#\n###\n" + "\n".join(log) + "\nHP: 10, Strength: 2"
        self.assertEqual(expected, stringed)

    def test_empty_arena(self):
        snapshot = Snapshot(WorldSnapshot(Arena(0, 0)), Pc(), [])
        self.assertRaises(Exception, lambda: snapshot_to_string(snapshot))

    def test_snapshot_none(self):
        self.assertRaises(Exception, lambda: snapshot_to_string(None))