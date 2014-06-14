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
        display(self.game.snapshot())
        while self.game.is_active():
            try:
                self.read_act_print()
            except Exception as e:
                logging.exception(e)

    def read_act_print(self):
        instr = get_input()
        action = translate(instr)
        if action is not None:
            out_snapshot = self.game.action(action)
            display(out_snapshot)
        else:
            print("bad input")


def get_input():
    return input("what do? ololo\n")


def translate(instr):
    if instr in stringToAction:
        return stringToAction[instr]
    else:
        return None


def display(out_snapshot):
    print(snapshot_printer.snapshot_to_string(out_snapshot))


if __name__ == '__main__':
    controller = CliController()
    controller.main()
