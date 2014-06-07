__author__ = 'python'

class Move:
    def __init__(self, direction):
        self.direction = direction

    def act(self, who, world):
        world.move(who, self.direction)