import random

import actions
import items
import spatial


__author__ = 'python'


class Character:
    def __init__(self, name="Manborg"):
        self.hp = 100
        self.strength = 10
        self.alive = True
        self.name = name
        self.types = []
        self.inventory = []

    def __eq__(self, other):
        return self.hp == other.hp \
               and self.strength == other.strength \
               and self.alive == other.alive \
               and self.name == other.name \
               and self.types == other.types \
               and self.inventory == other.inventory

    def __str__(self):
        return self.name

    def attack(self, enemy):
        enemy.hp -= self.strength

    def checkalive(self):
        if self.hp <= 0:
            self.alive = False
        return self.alive

    def kill(self):
        self.hp = -10

    def pickup(self, item):
        self.inventory.append(item)
        return item

    def itemdrop(self):
        return random.choice(self.inventory)

    def useitem(self, item):
        for power in item.powers:
            print(power)
            setattr(self, power, getattr(self, power) + item.powers[power])


class Npc(Character):
    def __init__(self, name):
        super().__init__(name)

    def findTarget(self, arena, point):
        minDist = 1000
        nearest = None
        for i, row in enumerate(arena.grid):
            for j, loc in enumerate(row):
                if loc.characters and self not in loc.characters:
                    if self.targetsAny(loc.characters):
                        distance = abs(i - point.x) + abs(j - point.y)
                        if distance < minDist:
                            minDist = distance
                            nearest = spatial.Point(i, j)
        return nearest

    def targetsAny(self, characters):
        for char in characters:
            if not char.types or self.types[0] not in char.types:
                return True
        return False


    def moveToward(self, point, loc):
        currX = point.x
        currY = point.y
        toX = loc.x
        toY = loc.y
        diffX = abs(currX - toX)
        diffY = abs(currY - toY)
        if (diffX == 0 or diffX <= diffY) and currY - toY > 0:
            return actions.Move("W")
        elif (diffX == 0 or diffX <= diffY) and currY - toY <= 0:
            return actions.Move("E")
        elif (diffY == 0 or diffX >= diffY) and currX - toX > 0:
            return actions.Move("N")
        elif (diffY == 0 or diffX >= diffY) and currX - toX <= 0:
            return actions.Move("S")

    def decide(self, arena):
        point = arena.findcharacter(self)
        t = self.findTarget(arena, point)
        if t:
            return self.moveToward(point, t)

        return actions.Rest()


class Pc(Character):
    def __init__(self):
        super().__init__()
        self.types.append("hero")
        self.inventory.append(items.Bone())