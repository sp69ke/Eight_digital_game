def is_valid_move(row, col, blank_row, blank_col):
    # 检查指定位置的格子是否可以移动到空白格子的位置
    if (row == blank_row and abs(col - blank_col) == 1) or \
            (col == blank_col and abs(row - blank_row) == 1):
        return True
    else:
        return False


class Board:
    def __init__(self, initial_state):
        self.size = 3
        self.state = initial_state

    def get_empty_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j
        return None

    def move_to_blank(self, row, col):
        # 检查指定位置的格子是否可以移动到空白格子的位置
        blank_row, blank_col = self.find_blank()

        if is_valid_move(row, col, blank_row, blank_col):
            # 交换指定位置的格子与空白格子的位置
            self.state[blank_row][blank_col], \
                self.state[row][col] = self.state[row][col], \
                self.state[blank_row][blank_col]

    def is_solved(self, target_state):
        return self.state == target_state

    def find_blank(self):
        # 查找空白格子的位置并返回其行列索引
        for row in range(self.size):
            for col in range(self.size):
                if self.state[row][col] == 0:
                    return row, col
