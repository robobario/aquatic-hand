__author__ = 'python'

def move(y):
    def second():
        print(y)
    return second

def pickup(y):
    return lambda: print(y)


def choose(x):
    if x:
        return move('something')
    else:
        return pickup('return')

choose(True)()
