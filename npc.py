import actions
from character import Character

__author__ = 'python'


class Npc(Character):
    def __init__(self, name):
        super().__init__(name)

    def decide(self, arena):
        return actions.Move('up')