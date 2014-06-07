import actions
from character import Character

__author__ = 'python'


class Npc(Character):
    def __init__(self):
        super().__init__()

    def decide(self, arena):
        return actions.Move('up')