__author__ = 'python'

class Move():
    def __init__(self, direction):
        self.direction = direction

    def act(self, who, world, log):
        world.move(who, self.direction, log)


class PickUp():
    def __init__(self):
        pass

    def act(self, who, world, log):
        world.pickup(who, log)


class Rest():
    def act(self, who, world, log):
        super().__init__()
        pass


class UseItem():
    def __init__(self):
        self.moreinfo = True
        self.where = 'character'

    def act(self, who, world, log):
        world.useitem(who, item, log)


class Query():
    def __init__(self, where):
        self.active = False
        self.where = where

    def act(self, who, world, log):
        return world.query(who, self.where)