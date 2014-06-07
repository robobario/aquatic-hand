from spacial import Point

__author__ = 'python'


class Arena:
    def __init__(self, width, height):
        self.grid = []
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

    def findcharacterlocation(self, character):
        return self.getlocation(self.findcharacter(character))

    def moveitem(self, item, to):
        self.getlocation(self.findcharacter(item)).removeitem(item)
        self.grid[to.x][to.y].additem(item)

    def ingrid(self, point):
        return 0 <= point.x < len(self.grid) and 0 <= point.y < len(self.grid[0])


class Location:
    def __init__(self):
        self.characters = []

    def __contains__(self, item):
        return item in self.characters

    def __len__(self):
        return len(self.characters)

    def additem(self, item):
        self.characters.append(item)

    def removeitem(self, item):
        if item in self:
            self.characters.remove(item)