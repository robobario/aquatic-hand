import logging

from actions import Move
from game import Game
from snapshot_printer import snapshotToString


__author__ = 'python'

logging.basicConfig(level=logging.DEBUG)

actions = {
    "up": Move("N"),
    "down": Move("S"),
    "left": Move("W"),
    "right": Move("E"),
    "upright": Move("NE"),
    "upleft": Move("NW"),
    "downright": Move("SE"),
    "downleft": Move("SW"),
}


class CliController:
    def __init__(self):
        self.game = Game()

    def main(self):
        self.display(self.game.snapshot())
        while self.game.isActive():
            try:
                self.readActPrint()
            except Exception as e:
                logging.exception(e)

    def readActPrint(self):
        instr = self.getinput()
        action = self.translate(instr)
        if action is not None:
            outsnapshot = self.game.action(action)
            self.display(outsnapshot)
        else:
            print("bad input")

    def getinput(self):
        return input("what do? ololo\n")

    def translate(self, instr):
        if instr in actions:
            return actions[instr]
        else:
            return None

    def display(self, outsnapshot):
        print(snapshotToString(outsnapshot))


if __name__ == '__main__':
    controller = CliController()
    controller.main()
