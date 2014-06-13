import character
import world

__author__ = 'python'


class Snapshot:
    def __init__(self, world_snapshot, hero, log):
        self.world_snapshot = world_snapshot
        self.hero = hero
        self.log = log


class Game:
    def __init__(self):
        self.world = world.World()
        self.hero = character.Pc()
        world.spawn(self.world.current, self.hero)
        self.active = True

    def is_active(self):
        return self.active

    def action(self, action):
        log = self.world.attempt(self.hero, action)
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, log)

    def snapshot(self):
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, [])

    def query(self, query):
        log = ['You have: \n']
        items = self.hero.inventory
        for item in len(items):
            log.append(item + ':' + str(items[item]) + '\,')
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero, log)