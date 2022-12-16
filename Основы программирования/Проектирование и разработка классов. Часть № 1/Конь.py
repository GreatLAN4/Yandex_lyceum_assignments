def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if abs(self.col - col) * abs(self.row - row) == 2 and self.row != row and self.col != col:
            return True
        return False