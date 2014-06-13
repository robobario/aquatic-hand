import random

from arena import Arena
from bestiary import Bestiary
from spatial import Point


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
        self.pcs = []
        self.npcs = []
        self.arena = arena


class World:
    def __init__(self):
        arena = Arena(12, 12)
        self.current = WorldSnapshot(arena)
        self.bestiary = Bestiary()
        self.genMobs = self.bestiary.getRandomMobs
        self.rng = lambda: random.randint(1, 100)

    def randomUnoccupiedPoint(self):
        def attempt(depth):
            if depth > 5:
                return None
            point = Point(self.rng() % self.current.arena.width, self.rng() % self.current.arena.height)
            if not self.current.arena.getlocation(point).characters:
                return point
            else:
                return attempt(depth + 1)

        return attempt(0)

    def spawn(self, snapshot, character):
        location = snapshot.arena.getlocation(self.randomUnoccupiedPoint())
        location.additem(character)

    def attempt(self, snapshot, who, action):
        log = []
        append = log.append
        self.pcaction(snapshot, who, action, append)
        self.npcaction(snapshot, append)
        self.spawnMobs(snapshot, append)
        self.checkdeaths(snapshot, append)
        return log

    def pcaction(self, snapshot, who, action, log):
        action.act(who, snapshot, self, log)

    def npcaction(self, snapshot, log):
        for npc in snapshot.npcs:
            action = npc.decide(snapshot.arena)
            action.act(npc, snapshot, self, log)

    def checkdeaths(self, snapshot, log):
        for character in snapshot.arena.getallcharacter():
            if not character.checkalive():
                snapshot.arena.findcharacterlocation(character).killcharacter(character)
                if character in snapshot.npcs:
                    snapshot.npcs.remove(character)

    def spawnMobs(self, snapshot, log):
        mobs = self.genMobs(snapshot.pcs)
        for mob in mobs:
            self.spawn(snapshot, mob)
            snapshot.npcs.append(mob)

    def snapshot(self):
        return self.current

    def move(self, snapshot, who, direction, log):
        point = snapshot.arena.findcharacter(who)
        to = point.add(directions[direction])
        if snapshot.arena.ingrid(to):
            tolocation = snapshot.arena.getlocation(to)
            if not tolocation.characters:
                snapshot.arena.moveitem(who, to)
                log(who.name + " moved " + direction)
            elif len(tolocation.characters) > 0 and who.types[0] not in tolocation.characters:
                who.attack(tolocation.characters[0])
                log(who.name + " attacked " + tolocation.characters[0].name)
            else:
                log(who.name + " can't move " + direction)
        for item in snapshot.arena.findcharacterlocation(who).items:
            log("You see a " + str(item) + " here.")

    def pickup(self, snapshot, who, log):
        location = snapshot.arena.findcharacterlocation(who)
        item = who.pickup(location.items.pop())
        log(who.name + " picks up " + str(item))





