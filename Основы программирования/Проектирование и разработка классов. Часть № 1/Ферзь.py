def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if abs(row - self.row) == abs(col - self.col):
            return True
        if self.col == col:
            return True
        if self.row == row:
            return True

        return False
