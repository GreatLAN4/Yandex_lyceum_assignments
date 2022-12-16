class SeaMap:
    def __init__(self):
        self.board = [[0 for _ in range(10)] for _ in range(10)]
        self.points = [".", "*", "x"]

    def shoot(self, x, y, result):
        if result == "miss":
            self.board[x][y] = 1

        elif result == "hit":
            self.board[x][y] = 2

        elif result == "sink":
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if self.board[i][j] == 0:
                            self.board[i][j] = 1
            self.board[x][y] = 2
            for j in range(10):
                if self.board[x][j] == 2:
                    col = j
                    for i in range(x - 1, x + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= u < 10:
                                if self.board[i][u] == 0:
                                    self.board[i][u] = 1
            for v in range(10):
                if self.board[v][y] == 2:
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(y - 1, y + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if self.board[v][u] == 0:
                                    self.board[v][u] = 1

    def cell(self, row, col):
        return self.points[self.board[row][col]]
