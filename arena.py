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
        for x in self.grid:
            for y in x:
                if character in y:
                    return Point(x, y)

    def moveitem(self, item, pointto):
        self.getlocation(self.findcharacter(item)).removeitem(item)
        self.grid[pointto.x, pointto.y].additem(item)


class Location:
    def __init__(self):
        self.contains = []

    def __contains__(self, item):
        return item in self.contains

    def __len__(self):
        return len(self.contains)

    def additem(self, item):
        self.contains.append(item)

    def removeitem(self, item):
        if item in self:
            self.contains.remove(item)