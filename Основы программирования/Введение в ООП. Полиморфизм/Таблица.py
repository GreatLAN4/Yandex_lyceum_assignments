class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.field = [[0 for _ in range(cols)] for _ in range(rows)]

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def get_value(self, row, col):
        return (self.field[row][col] if 0 <= row < self.rows and 0 <= col < self.cols
                else None)

    def set_value(self, row, col, value):
        self.field[row][col] = value
