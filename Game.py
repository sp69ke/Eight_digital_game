import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.window_size = (320, 320)
        self.surface = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.fps = 30

    def start(self):
        # 主循环
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
