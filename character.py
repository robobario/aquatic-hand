__author__ = 'python'


class Character:
    def __init__(self, name="Manborg"):
        self.hp = 100
        self.strength = 10
        self.alive = True
        self.name = name

    def attack(self, enemy):
        enemy.hp -= self.strength

    def checkdead(self):
        if self.hp <= 0:
            self.alive = False
