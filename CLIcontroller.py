import logging

import actions
import game
import queries
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

class QueryAndHandler:
    def __init__(self, query, handler=snapshot_printer.print_inventory):
        self.query = query
        self.handler = handler

stringToQuery = {
    'inventory': QueryAndHandler(queries.inventory)
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
        action = translate(instr, self.game)
        action()


def action_curry(action, this_game):
    def inner():
        out_snapshot = this_game.action(action)
        display(out_snapshot)

    return inner


def query_curry(query_and_handler, this_game):
    def inner():
        result = this_game.query(query_and_handler.query)
        query_and_handler.handler(result)
        pass

    return inner


def get_input():
    return input("what do? ololo\n")


def translate(instr, this_game):
    if instr in stringToAction:
        return action_curry(stringToAction[instr], this_game)
    elif instr in stringToQuery:
        return query_curry(stringToQuery[instr], this_game)
    else:
        return lambda: print('bad input')


def display(out_snapshot):
    print(snapshot_printer.snapshot_to_string(out_snapshot))


if __name__ == '__main__':
    controller = CliController()
    controller.main()
