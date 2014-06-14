import random

import actions
import items
import spatial


__author__ = 'python'

char_id = 1


def next_id():
    global char_id
    char_id += 1
    return char_id


class Character:
    def __init__(self, name="Manborg"):
        self.hp = 100
        self.strength = 10
        self.alive = True
        self.name = name
        self.types = []
        self.inventory = []
        self.id = next_id()

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.name

    def attack(self, enemy):
        enemy.hp -= self.strength

    def check_alive(self):
        if self.hp <= 0:
            self.alive = False
        return self.alive

    def kill(self):
        self.hp = -10

    def pickup(self, item):
        self.inventory.append(item)
        return item

    def item_drop(self):
        return random.choice(self.inventory)

    def use_item(self, item):
        for power in item.powers:
            print(power)
            setattr(self, power, getattr(self, power) + item.powers[power])


class Npc(Character):
    def __init__(self, name):
        super().__init__(name)

    def find_target(self, arena, point):
        min_dist = 1000
        nearest = None
        for i, row in enumerate(arena.grid):
            for j, loc in enumerate(row):
                if loc.characters and self not in loc.characters:
                    if self.targets_any(loc.characters):
                        distance = abs(i - point.x) + abs(j - point.y)
                        if distance < min_dist:
                            min_dist = distance
                            nearest = spatial.Point(i, j)
        return nearest

    def targets_any(self, characters):
        for char in characters:
            if not char.types or self.types[0] not in char.types:
                return True
        return False

    def decide(self, arena):
        point = arena.find_character(self)
        t = self.find_target(arena, point)
        if t:
            return move_toward(point, t)

        return actions.Rest()


def move_toward(point, loc):
    curr_x = point.x
    curr_y = point.y
    to_x = loc.x
    to_y = loc.y
    diff_x = abs(curr_x - to_x)
    diff_y = abs(curr_y - to_y)
    if (diff_x == 0 or diff_x <= diff_y) and curr_y - to_y > 0:
        return actions.Move("W")
    elif (diff_x == 0 or diff_x <= diff_y) and curr_y - to_y <= 0:
        return actions.Move("E")
    elif (diff_y == 0 or diff_x >= diff_y) and curr_x - to_x > 0:
        return actions.Move("N")
    elif (diff_y == 0 or diff_x >= diff_y) and curr_x - to_x <= 0:
        return actions.Move("S")


class Pc(Character):
    def __init__(self):
        super().__init__()
        self.types.append("hero")
        self.inventory.append(items.Bone())