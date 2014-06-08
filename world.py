import random

from arena import Arena
from bestiary import Bestiary
from spacial import Point


__author__ = 'python'

directions = {
    "N": Point(-1, 0),
    "S": Point(1, 0),
    "W": Point(0, -1),
    "E": Point(0, 1),
    "NE": Point(-1, 1),
    "NW": Point(-1, -1),
    "SE": Point(1, 1),
    "SW": Point(1, -1)
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
            action.act(npc, self, log)

    def checkdeaths(self, log):
        for character in self.arena.getallcharacter():
            if not character.checkalive():
                self.arena.findcharacterlocation(character).killcharacter(character)
                if character in self.npcs:
                    self.npcs.remove(character)

    def spawnMobs(self, log):
        mobs = self.genMobs(self.pcs)
        for mob in mobs:
            self.spawn(mob)
            self.npcs.append(mob)

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
            elif len(tolocation.characters) > 0 and who.types[0] not in tolocation.characters:
                who.attack(tolocation.characters[0])
                log(who.name + " attacked " + tolocation.characters[0].name)
            else:
                log(who.name + " can't move " + direction)
        for item in self.arena.findcharacterlocation(who).items:
            log("You see a " + str(item) + " here.")

    def pickup(self, who, log):
        location = self.arena.findcharacterlocation(who)
        item = who.pickup(location.items.pop())
        log(who.name + " picks up " + str(item))





