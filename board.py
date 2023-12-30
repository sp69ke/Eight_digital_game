class NumberTile:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def draw(self, surface, font):
        if self.value != 0:
            text = font.render(str(self.value), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (self.x + 50, self.y + 50)
            surface.blit(text, text_rect)