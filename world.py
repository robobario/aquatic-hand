import copy

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
    def __init__(self, current_arena):
        self.pcs = []
        self.npcs = []
        self.arena = current_arena


class World:
    def __init__(self):
        an_arena = arena.Arena(12, 12)
        self.current = WorldSnapshot(an_arena)
        self.bestiary = bestiary.Bestiary()
        self.genMobs = self.bestiary.get_random_mobs

    def attempt(self, hero_id, action):
        new_state = copy.deepcopy(self.current)
        log = do_attempt(self.genMobs, new_state, hero_id, action)
        self.current = new_state
        return log

    def snapshot(self):
        return self.current


def do_attempt(gen_mobs, snapshot, hero_id, action):
    log = []
    append = log.append
    pc_action(snapshot, hero_id, action, append)
    npc_action(snapshot, append)
    mobs = gen_mobs(snapshot.pcs)
    spawn_mobs(snapshot, mobs)
    check_deaths(snapshot)
    return log


def check_deaths(snapshot):
    for character in snapshot.arena.getallcharacter():
        if not character.check_alive():
            snapshot.arena.findcharacterlocation(character).killcharacter(character)
            if character in snapshot.npcs:
                snapshot.npcs.remove(character)


def pc_action(snapshot, hero_id, action, log):
    action.act(hero_id, snapshot, log)


def npc_action(snapshot, log):
    for npc in snapshot.npcs:
        action = npc.decide(snapshot.arena)
        action.act(npc.id, snapshot, log)


def spawn_mobs(snapshot, mobs):
    for mob in mobs:
        spawn(snapshot, mob)
        snapshot.npcs.append(mob)


def spawn(snapshot, character):
    location = snapshot.arena.getlocation(snapshot.arena.randomUnoccupiedPoint())
    location.additem(character)


def move(snapshot, hero_id, direction, log):
    who = snapshot.arena.find(hero_id)
    point = snapshot.arena.findcharacter(who)
    to = point.add(directions[direction])
    if snapshot.arena.ingrid(to):
        to_location = snapshot.arena.getlocation(to)
        if not to_location.characters:
            snapshot.arena.moveitem(who, to)
            log(who.name + " moved " + direction)
        elif len(to_location.characters) > 0 and who.types[0] not in to_location.characters[0].types:
            who.attack(to_location.characters[0])
            log(who.name + " attacked " + to_location.characters[0].name)
        else:
            log(who.name + " can't move " + direction)
    for item in snapshot.arena.findcharacterlocation(who).items:
        log("You see a " + str(item) + " here.")


def pickup(snapshot, hero_id, log):
    who = snapshot.arena.find(hero_id)
    location = snapshot.arena.findcharacterlocation(who)
    item = who.pickup(location.items.pop())
    log(who.name + " picks up " + str(item))