import copy
import random

import spatial


__author__ = 'python'


class Arena:
    def __init__(self, width, height):
        self.grid = []
        self.width = width
        self.height = height
        self.rng = lambda: random.randint(1, 100)
        for x in range(height):
            row = []
            self.grid.append(row)
            for y in range(width):
                row.append(Location())

    def get_location(self, point):
        return self.grid[point.x][point.y]

    def find_character(self, character):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if character in self.grid[x][y]:
                    return spatial.Point(x, y)

    def get_all_character(self):
        all_characters = []
        for x in self.grid:
            for y in x:
                for z in y.characters:
                    all_characters.append(z)
        return all_characters

    def find_character_location(self, character):
        return self.get_location(self.find_character(character))

    def find(self, character_id):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                for char in self.grid[x][y].characters:
                    if char.id == character_id:
                        return char
        return None

    def move_item(self, item, to):
        self.get_location(self.find_character(item)).removeitem(item)
        self.grid[to.x][to.y].additem(item)

    def ingrid(self, point):
        return 0 <= point.x < len(self.grid) and 0 <= point.y < len(self.grid[0])

    def copy(self):
        return copy.deepcopy(self)

    def random_unoccupied_point(self):
        def attempt(depth):
            if depth > 5:
                return None
            point = spatial.Point(self.rng() % self.width, self.rng() % self.height)
            if not self.get_location(point).characters:
                return point
            else:
                return attempt(depth + 1)

        return attempt(0)


class Location:
    def __init__(self):
        self.characters = []
        self.items = []

    def __contains__(self, item):
        return item in self.characters

    def __len__(self):
        return len(self.characters + self.items)

    def additem(self, item):
        self.characters.append(item)

    def removeitem(self, item):
        if item in self:
            self.characters.remove(item)

    def killcharacter(self, character):
        self.items.append(character.item_drop())
        self.removeitem(character)

    def getprintitem(self):
        if len(self.characters) > 0:
            return self.characters[0]
        elif len(self.items) > 0:
            return self.items[0]
        return False