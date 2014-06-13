__author__ = 'python'

symbols = {
    "cat": "x",
    "basic": "\'",
    "fancy": "*"
}


def get_arena(snapshot):
    world = snapshot.world_snapshot
    if world is None:
        raise Exception('world is none')
    arena = world.arena
    if arena is None:
        raise Exception('world has no arena')
    if arena.grid is None or len(arena.grid) == 0:
        raise Exception('arena grid is none or empty')
    return arena


def print_log(log):
    if log:
        return "\n".join(log) + "\n"
    else:
        return ""


def snapshot_to_string(snapshot):
    if snapshot is None:
        raise Exception('snapshot is none')
    arena = get_arena(snapshot)
    result = print_grid(arena)
    hero = snapshot.hero
    result += print_log(snapshot.log)
    result += print_hero(hero)
    return result


def symbol_for_location(location):
    print_item = location.getprintitem()
    if print_item:
        type = print_item.types[0]
        if type in symbols:
            return symbols[type]
    return "\u263A"


def print_row(row):
    result = ""
    for location in row:
        if len(location) > 0:
            result += symbol_for_location(location)
        else:
            result += ' '
    return result


def print_grid(arena):
    result = ""
    result += "#" * (len(arena.grid[0]) + 2) + "\n"
    for row in arena.grid:
        result += "#" + print_row(row) + "#" + "\n"
    result += "#" * (len(arena.grid) + 2) + "\n"
    return result


def print_hero(hero):
    return "HP: " + str(hero.hp) + ", Strength: " + str(hero.strength)