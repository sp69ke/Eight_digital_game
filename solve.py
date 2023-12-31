import numpy as np


class Astar:
    def __init__(self, board):
        self.board = board
        self.end = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.open = board.state
        self.close = []

    def calcDistH(self):
        cost = 0
        for i in range(len(self.board.state)):
            if self.board.state[i] != 0:
                cost += abs(int(self.board.state[i]) // 3 - i // 3) + \
                        abs(int(self.board.state[i]) % 3 - i % 3)
        return cost
