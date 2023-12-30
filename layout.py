import pygame
from board import *


class Layout:
    def __init__(self):
        self.tiles = []
        self.font = pygame.font.Font(None, 50)
        self.tile_size = 100
        self.margin = 10

        for i in range(3):
            for j in range(3):
                tile = NumberTile(i * 3 + j, j * (self.tile_size + self.margin) + self.margin,
                                  i * (self.tile_size + self.margin) + self.margin)
                self.tiles.append(tile)

    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface, self.font)
