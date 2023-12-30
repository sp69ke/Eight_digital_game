import sys
import pygame
from pygame.locals import *

blocks = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}


def drawTable(screen):
    pygame.draw.rect(screen, Color("black"), (50, 50, 500, 500), 1)


def startGame():
    # init
    pygame.init()
    size = width, height = 800, 600
    bg_color = (255, 255, 255)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("八数码游戏")

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(bg_color)
        drawTable(screen)
        pygame.display.update()


if __name__ == "__main__":
    startGame()
