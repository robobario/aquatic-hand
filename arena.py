import copy
import random

from spatial import Point


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

    def getlocation(self, point):
        return self.grid[point.x][point.y]

    def findcharacter(self, character):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if character in self.grid[x][y]:
                    return Point(x, y)

    def getallcharacter(self):
        allcharacters = []
        for x in self.grid:
            for y in x:
                for z in y.characters:
                    allcharacters.append(z)
        return allcharacters

    def findcharacterlocation(self, character):
        return self.getlocation(self.findcharacter(character))

    def moveitem(self, item, to):
        self.getlocation(self.findcharacter(item)).removeitem(item)
        self.grid[to.x][to.y].additem(item)

    def ingrid(self, point):
        return 0 <= point.x < len(self.grid) and 0 <= point.y < len(self.grid[0])

    def copy(self):
        return copy.deepcopy(self)

    def randomUnoccupiedPoint(self):
        def attempt(depth):
            if depth > 5:
                return None
            point = Point(self.rng() % self.width, self.rng() % self.height)
            if not self.getlocation(point).characters:
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
        self.items.append(character.itemdrop())
        self.removeitem(character)

    def getprintitem(self):
        if len(self.characters) > 0:
            return self.characters[0]
        elif len(self.items) > 0:
            return self.items[0]
        return False