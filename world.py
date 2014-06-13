import random

import arena
import bestiary
import spatial


__author__ = 'python'

directions = {
    "N": spatial.Point(-1, 0),
    "S": spatial.Point(1, 0),
    "W": spatial.Point(0, -1),
    "E": spatial.Point(0, 1),
    "NE": spatial.Point(-1, 1),
    "NW": spatial.Point(-1, -1),
    "SE": spatial.Point(1, 1),
    "SW": spatial.Point(1, -1)
}


class WorldSnapshot:
    def __init__(self, arena):
        self.pcs = []
        self.npcs = []
        self.arena = arena


class World:
    def __init__(self):
        anArena = arena.Arena(12, 12)
        self.current = WorldSnapshot(anArena)
        self.bestiary = bestiary.Bestiary()
        self.genMobs = self.bestiary.getRandomMobs
        self.rng = lambda: random.randint(1, 100)

    def spawn(self, snapshot, character):
        location = snapshot.arena.getlocation(snapshot.arena.randomUnoccupiedPoint())
        location.additem(character)

    def attempt(self, snapshot, who, action):
        log = []
        append = log.append
        pcaction(snapshot, who, action, append)
        npcaction(snapshot, append)
        mobs = self.genMobs(snapshot.pcs)
        spawnMobs(snapshot, mobs)
        checkdeaths(snapshot)
        return log

    def snapshot(self):
        return self.current


def checkdeaths(snapshot):
    for character in snapshot.arena.getallcharacter():
        if not character.checkalive():
            snapshot.arena.findcharacterlocation(character).killcharacter(character)
            if character in snapshot.npcs:
                snapshot.npcs.remove(character)


def pcaction(snapshot, who, action, log):
    action.act(who, snapshot, log)


def npcaction(snapshot, log):
    for npc in snapshot.npcs:
        action = npc.decide(snapshot.arena)
        action.act(npc, snapshot, log)


def spawnMobs(snapshot, mobs):
    for mob in mobs:
        spawn(snapshot, mob)
        snapshot.npcs.append(mob)


def spawn(snapshot, character):
    location = snapshot.arena.getlocation(snapshot.arena.randomUnoccupiedPoint())
    location.additem(character)


def move(snapshot, who, direction, log):
    point = snapshot.arena.findcharacter(who)
    to = point.add(directions[direction])
    if snapshot.arena.ingrid(to):
        to_location = snapshot.arena.getlocation(to)
        if not to_location.characters:
            snapshot.arena.moveitem(who, to)
            log(who.name + " moved " + direction)
        elif len(to_location.characters) > 0 and who.types[0] not in to_location.characters:
            who.attack(to_location.characters[0])
            log(who.name + " attacked " + to_location.characters[0].name)
        else:
            log(who.name + " can't move " + direction)
    for item in snapshot.arena.findcharacterlocation(who).items:
        log("You see a " + str(item) + " here.")


def pickup(snapshot, who, log):
    location = snapshot.arena.findcharacterlocation(who)
    item = who.pickup(location.items.pop())
    log(who.name + " picks up " + str(item))