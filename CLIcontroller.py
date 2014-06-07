from actions import Move
from game import Game

__author__ = 'python'

map = {
    "up": Move("up")
}

class CliController:

    def __init__(self):
        self.game = Game()

    def main(self):
        while self.game.isActive():
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
        if instr in map:
            return map[instr]
        else:
            return None


    def display(self, outsnapshot):
        pass


if __name__ == '__main__':
    controller = CliController()
    controller.main()
