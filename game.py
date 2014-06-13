import character
import world

__author__ = 'python'


class Snapshot:
    def __init__(self, world_snapshot, hero_id, log):
        self.world_snapshot = world_snapshot
        self.hero_id = hero_id
        self.log = log


class Game:
    def __init__(self):
        self.world = world.World()
        hero = character.Pc()
        self.hero_id = hero.id
        self.world.spawn(hero)
        self.active = True

    def is_active(self):
        return self.active

    def action(self, action):
        log = self.world.attempt(self.hero_id, action)
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero_id, log)

    def snapshot(self):
        snap = self.world.snapshot()
        return Snapshot(snap, self.hero_id, [])

