import pygame
from layout import Layout


class Game:
    def __init__(self):
        pygame.init()

        self.window_size = (320, 320)
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Eight Puzzle Game")
        self.clock = pygame.time.Clock()
        self.fps = 30

    def start(self):
        layout = Layout()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.surface.fill((0, 0, 0))
            layout.draw(self.surface)

            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
