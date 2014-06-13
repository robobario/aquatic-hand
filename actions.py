import world

__author__ = 'python'


class Move:
    def __init__(self, direction):
        self.direction = direction

    def act(self, snapshot, who, log):
        world.move(who, snapshot, self.direction, log)


class PickUp:
    def __init__(self):
        pass

    def act(self, snapshot, who, log):
        world.pickup(who, snapshot, log)

class Rest:
    def act(self, snapshot, who, log):
        pass