import character
import world

__author__ = 'python'


class Snapshot:
    def __init__(self, worldsnap, hero, log):
        self.worldsnap = worldsnap
        self.hero = hero
        self.log = log


class Game:
    def __init__(self):
        self.world = world.World()
        self.hero = character.Pc()
        self.world.spawn(self.world.current, self.hero)
        self.active = True

    def isActive(self):
        return self.active

    def action(self, action):
        log = self.world.attempt(self.world.current, self.hero, action)
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, log)

    def snapshot(self):
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, [])

