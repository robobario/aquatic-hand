__author__ = 'python'


class Move:
    def __init__(self, direction):
        self.direction = direction

    def act(self, who, world, log):
        world.move(who, self.direction, log)


class Rest:
    def act(self, who, world, log):
        pass