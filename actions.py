import world

__author__ = 'python'


class Move:
    def __init__(self, direction):
        self.direction = direction

    def act(self, snapshot, hero_id, log):
        world.move(hero_id, snapshot, self.direction, log)


class PickUp:
    def __init__(self):
        pass

    def act(self, snapshot, hero_id, log):
        world.pickup(hero_id, snapshot, log)


class Rest:
    def act(self, snapshot, hero_id, log):
        pass