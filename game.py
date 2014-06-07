from pc import Pc
from world import World

__author__ = 'python'


class Snapshot:
    def __init__(self, worldsnap, hero):
        self.worldsnap = worldsnap
        self.hero = hero


class Game:
    def __init__(self):
        self.world = World()
        self.hero = Pc()
        self.world.spawn(self.hero)
        self.active = True

    def isActive(self):
        return self.active

    def action(self, action):
        worldsnap = self.world.attempt(self.hero, action)
        return Snapshot(worldsnap, self.hero)

