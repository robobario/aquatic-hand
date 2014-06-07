import random

from npc import Npc


__author__ = 'python'


class Bestiary:
    def __init__(self):
        self.rng = lambda: random.randint(1, 5)

    def getRandomMobs(self, heroes):
        mobs = []
        if self.rng() % 5 == 0:
            mobs.append(Cat())
        return mobs


class Cat(Npc):
    def __init__(self):
        super().__init__("cat")
        self.hp = 10
        self.strength = 2

    pass