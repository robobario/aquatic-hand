from game import Game

__author__ = 'python'


class CliController:
    def __init__(self):
        self.game = Game()

    def main(self):
        while self.game.active():
            instr = self.getinput()
            outsnapshot = self.game.action(self.translate(instr))
            self.display(outsnapshot)

    def getinput(self):
        return ''

    def translate(self, instr):
        pass

    def display(self, outsnapshot):
        pass


if __name__ == '__main__':
    controller = CliController()
    controller.main()
