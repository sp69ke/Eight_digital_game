import pygame

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# 定义字体
FONT_SIZE = 36
FONT_NAME = 'Arial'


class Layout:
    def __init__(self):
        self.cell_width = 200
        self.cell_height = 200
        self.board_width = self.cell_width * 3
        self.board_height = self.cell_height * 3

    def draw_board(self, screen, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell_value = board[i][j]
                # 计算绘制位置
                x = j * self.cell_width
                y = i * self.cell_height

                # 绘制方格
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, self.cell_width, self.cell_height), 0)
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, self.cell_width, self.cell_height), 1)

                # 绘制数字
                if cell_value != 0:
                    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
                    text = font.render(str(cell_value), True, BLACK)
                    text_rect = text.get_rect(center=(x + self.cell_width / 2, y + self.cell_height / 2))
                    screen.blit(text, text_rect)

    def draw_message(self, screen, message):
        font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        text = font.render(message, True, RED)
        text_rect = text.get_rect(center=(self.board_width / 2, self.board_height + 50))
        screen.blit(text, text_rect)
