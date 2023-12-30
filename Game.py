import pygame
from board import Board
from layout import Layout


class Game:
    def __init__(self, board, target_state):
        self.board = board
        self.target_state = target_state
        self.layout = Layout()
        self.screen = pygame.display.set_mode((self.layout.board_width, self.layout.board_height + 100))
        pygame.display.set_caption("Eight Puzzle")

    def handle_input(self):
        # 处理键盘输入和鼠标点击事件
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.board.move('up')
                elif event.key == pygame.K_DOWN:
                    self.board.move('down')
                elif event.key == pygame.K_LEFT:
                    self.board.move('left')
                elif event.key == pygame.K_RIGHT:
                    self.board.move('right')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_row = mouse_pos[1] // self.layout.cell_height
                    clicked_col = mouse_pos[0] // self.layout.cell_width
                    self.board.move_to_blank(clicked_row, clicked_col)

    def draw(self):
        # 绘制游戏界面
        self.screen.fill((255, 255, 255))
        self.layout.draw_board(self.screen, self.board.state)
        if self.board.is_solved(self.target_state):
            self.layout.draw_message(self.screen, 'Congratulations!')
        pygame.display.flip()

    def run(self):
        # 游戏主循环
        pygame.init()
        clock = pygame.time.Clock()

        while not self.board.is_solved(self.target_state):
            self.handle_input()
            self.draw()
            clock.tick(60)

        pygame.quit()
