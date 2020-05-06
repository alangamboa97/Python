#TicTacToe game in python

class Counter:

    def __init__ (self, string):
        self.label = string
    def __str__(self):
        return self.label

X = Counter('X') #definimos variables
O = Counter('O')



class Move:
     #   representa el movimiento realizado por el jugador

    def __init__(self, counter, x, y):
        self.x = x
        self.y = y
        self.counter = counter

class Player:(metaclass=ABCMeta):
    