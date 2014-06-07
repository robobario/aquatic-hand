__author__ = 'python'


class Arena:
    def __init__(self, width, height):
        self.grid = []
        for i in range(height):
            row = []
            self.grid.append(row)
            for j in range(width):
                row.append(location())

    def getlocation(self, point):
        return self.grid[point.x][point.y]


class location:
    def __init__(self):
        self.contains = []

    def __contains__(self, item):
        return item in self.contains
