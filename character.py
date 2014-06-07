import actions

__author__ = 'python'


class Character:
    def __init__(self, name="Manborg"):
        self.hp = 100
        self.strength = 10
        self.alive = True
        self.name = name
        self.types = []

    def attack(self, enemy):
        enemy.hp -= self.strength

    def checkdead(self):
        if self.hp <= 0:
            self.alive = False


class Npc(Character):
    def __init__(self, name):
        super().__init__(name)

    def decide(self, arena):
        return actions.Move('up')


class Pc(Character):
    def __init__(self):
        super().__init__()