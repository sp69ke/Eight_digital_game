from board import Board
from Game import Game
import random
import pyautogui

initial_state = []
target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
target_state_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def makeBoard():
    # 生成随机矩阵并保证有解
    def isValid(list1, list2):
        # 逆序和相等
        sum1 = sum2 = 0
        for i in range(8):
            for j in range(8):
                if list1[i] > list1[j] and i < j:
                    sum1 += 1
                if list2[i] > list2[j] and i < j:
                    sum2 += 1
        return sum1 // 2 == sum2 // 2

    random_list = random.sample(range(0, 9), 9)
    # print(random_list)
    while not isValid(random_list, target_state_list):
        random_list = random.sample(range(0, 9), 9)

    for i in range(3):
        initial_state.append([])
        for j in range(i * 3 - 3, i * 3):
            initial_state[i].append(random_list[j])
    # print(initial_state)
    # print(isValid(random_list, target_state_list))


def main():
    makeBoard()
    board = Board(initial_state)
    game = Game(board, target_state)
    game.run()


main()

'''
pyinstaller main.py -p board.py -p Game.py -p layout.py -p solve.py --hidden-import numpy --hidden-import pyautogui --hidden-import pygame 
以上为一整条命令 
'''