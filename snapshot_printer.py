__author__ = 'python'


def getArena(snapshot):
    world = snapshot.worldsnap
    if world is None:
        raise Exception('world is none')
    arena = world.arena
    if arena is None:
        raise Exception('world has no arena')
    if arena.grid is None or len(arena.grid) == 0:
        raise Exception('arena grid is none or empty')
    return arena


def snapshotToString(snapshot):
    if snapshot is None:
        raise Exception('snapshot is none')
    arena = getArena(snapshot)
    result = printGrid(arena)
    hero = snapshot.hero
    result += printHero(hero)
    return result


def symbolForLocation(location):
    first = location.characters[0]
    if "cat" in first.types:
        return "x"
    return '0'


def printRow(row):
    result = ""
    for location in row:
        if len(location) > 0:
            result += symbolForLocation(location)
        else:
            result += ' '
    return result


def printGrid(arena):
    result = ""
    result += "#" * (len(arena.grid[0]) + 2) + "\n"
    for row in arena.grid:
        result += "#" + printRow(row) + "#" + "\n"
    result += "#" * (len(arena.grid) + 2) + "\n"
    return result


def printHero(hero):
    return "HP: " + str(hero.hp) + ", Strength: " + str(hero.strength)