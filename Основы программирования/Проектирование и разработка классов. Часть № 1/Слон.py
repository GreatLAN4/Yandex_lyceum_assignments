def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False
