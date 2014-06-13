from character import Pc
from world import World

__author__ = 'python'


class Snapshot:
    def __init__(self, worldsnap, hero, log):
        self.worldsnap = worldsnap
        self.hero = hero
        self.log = log


class Game:
    def __init__(self):
        self.world = World()
        self.hero = Pc()
        self.world.spawn(self.hero)
        self.active = True

    def isActive(self):
        return self.active

    def action(self, action):
        log = self.world.attempt(self.hero, action)
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, log)

    def query(self, query):
        log = self.world.query(self.hero, query)
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, log)

    def snapshot(self):
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, [])

