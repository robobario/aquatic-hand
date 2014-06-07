__author__ = 'python'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def gettuple(self):
        return self.x, self.y
