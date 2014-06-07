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
        self.pcs.append(character)

    def attempt(self, who, action):
        log = []
        append = log.append
        self.pcaction(who, action, append)
        self.npcaction(append)
        self.spawnMobs(append)
        self.checkdeaths(append)
        return log

    def pcaction(self, who, action, log):
        action.act(who, self, log)

    def npcaction(self, log):
        for npc in self.npcs:
            action = npc.decide(self.arena)
            action.act(npc, self)

    def checkdeaths(self, log):
        for character in self.npcs + self.pcs:
            character.checkalive()

    def spawnMobs(self, log):
        mobs = self.genMobs(self.pcs)
        for mob in mobs:
            self.spawn(mob)

    def snapshot(self):
        return WorldSnapshot(self.arena)

    def move(self, who, direction, log):
        point = self.arena.findcharacter(who)
        to = point.add(directions[direction])
        if self.arena.ingrid(to):
            tolocation = self.arena.getlocation(to)
            if not tolocation.characters:
                self.arena.moveitem(who, to)
                log(who.name + " moved " + direction)
            elif len(tolocation.characters) > 0:
                who.attack(tolocation.characters[0])
                log(who.name + " attacket " + tolocation.characters[0].name)





