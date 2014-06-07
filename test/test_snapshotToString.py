from unittest import TestCase
from arena import Arena
from game import Snapshot
from pc import Pc
from snapshot_printer import snapshotToString
from world import WorldSnapshot

__author__ = 'python'


class TestSnapshotToString(TestCase):
    def test_snapshotToString(self):
        snapshot = Snapshot(WorldSnapshot(Arena(1,1)), Pc())
        stringed = snapshotToString(snapshot)
        expected = "###\n# #\n###\nHP: 100, Strength: 10"
        self.assertEqual(expected,stringed)

    def test_emptyArena(self):
        snapshot = Snapshot(WorldSnapshot(Arena(0,0)), Pc())
        self.assertRaises(Exception, lambda: snapshotToString(snapshot))

    def test_snapshotNone(self):
        self.assertRaises(Exception, lambda: snapshotToString(None))