from board import Board
from Game import Game

initial_state = [[2, 1, 3], [4, 5, 6], [7, 8, 0]]

target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def main():
    board = Board(initial_state)
    game = Game(board, target_state)
    game.run()


# if __name__ == "main":
main()
