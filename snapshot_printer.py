__author__ = 'python'


def snapshotToString(snapshot):
    if snapshot is None:
        return None
    world = snapshot.worldsnap
    arena = world.arena
    result = printGrid(arena)
    hero = snapshot.hero
    result += printHero(hero)
    return result


def printGrid(arena):
    result = ""
    result += "#" * (len(arena.grid[0]) + 2) + "\n"
    for row in arena.grid:
        result += "#" + " " * len(row) + "#" + "\n"
    result += "#" * (len(arena.grid) + 2) + "\n"
    return result


def printHero(hero):
    return "HP: " + str(hero.hp) + ", Strength: " + str(hero.strength)