from spacial import Point

__author__ = 'python'


class Arena:
    def __init__(self, width, height):
        self.grid = []
        for i in range(height):
            row = []
            self.grid.append(row)
            for j in range(width):
                row.append(Location())

    def getlocation(self, point):
        return self.grid[point.x][point.y]

    def findcharacter(self, character):
        for x in self.grid:
            for y in self.grid[x]:
                if character in self.grid[x][y]:
                    return Point(x, y)


class Location:
    def __init__(self):
        self.contains = []

    def __contains__(self, item):
        return item in self.contains
