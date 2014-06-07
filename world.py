import random

from arena import Arena
from bestiary import Bestiary
from spacial import Point


__author__ = 'python'

directions = {
    "up": Point(-1, 0),
    "down": Point(1, 0),
    "left": Point(0, -1),
    "right": Point(0, 1)
}


class WorldSnapshot:
    def __init__(self, arena):
        self.arena = arena


class World:
    def __init__(self):
        self.pcs = []
        self.npcs = []
        self.width = 12
        self.height = 12
        self.arena = Arena(self.width, self.height)
        self.bestiary = Bestiary()
        self.genMobs = self.bestiary.getRandomMobs
        self.rng = lambda: random.randint(1, 100)

    def randomUnoccupiedPoint(self):
        def attempt(depth):
            if depth > 5:
                return None
            point = Point(self.rng() % self.width, self.rng() % self.height)
            if not self.arena.getlocation(point).characters:
                return point
            else:
                return attempt(depth + 1)

        return attempt(0)

    def spawn(self, character):
        location = self.arena.getlocation(self.randomUnoccupiedPoint())
        location.additem(character)

    def attempt(self, who, action):
        self.pcaction(who, action)
        self.npcaction()
        self.spawnMobs()
        return self.snapshot()

    def pcaction(self, who, action):
        action.act(who, self)

    def npcaction(self):
        for npc in self.npcs:
            action = npc.decide(self.arena)
            action.act(npc, self)

    def snapshot(self):
        return WorldSnapshot(self.arena)

    def move(self, who, direction):
        point = self.arena.findcharacter(who)
        pointto = point.add(directions[direction])
        if not self.arena.getlocation(pointto).characters and self.arena.ingrid(pointto):
            self.arena.moveitem(who, pointto)

    def spawnMobs(self):
        mobs = self.genMobs(self.pcs)
        for mob in mobs:
            self.spawn(mob)





