import logging

import actions
import game
import snapshot_printer


__author__ = 'python'

logging.basicConfig(level=logging.DEBUG)

stringToAction = {
    "up": actions.Move("N"),
    "down": actions.Move("S"),
    "left": actions.Move("W"),
    "right": actions.Move("E"),
    "upright": actions.Move("NE"),
    "upleft": actions.Move("NW"),
    "downright": actions.Move("SE"),
    "downleft": actions.Move("SW"),
    "pickup": actions.PickUp()
}


class CliController:
    def __init__(self):
        self.game = game.Game()

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
        if instr in stringToAction:
            return stringToAction[instr]
        else:
            return None

    def display(self, outsnapshot):
        print(snapshot_printer.snapshotToString(outsnapshot))


if __name__ == '__main__':
    controller = CliController()
    controller.main()
