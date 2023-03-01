import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.RenderBoard()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.RenderBoard()

    # настройка внешнего вида
    def RenderBoard(self):

        self.board = [[[self.left + (x * self.cell_size), self.top + (y * self.cell_size)]
                       for x in range(self.width)] for y in range(self.height)]

    def render(self, screen):
        for line in self.board:
            for cord in line:
                x, y = cord
                pygame.draw.rect(screen, "white", pygame.Rect(x, y, self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def check(self):
        for line in self.board:
            print(line)

    def get_cell(self, mouse_pos):
        x_mouse, y_mouse = mouse_pos
        cells_poss = self.board[0]
        if cells_poss[0][0] <= x_mouse <= cells_poss[-1][-2]:
            pass
        else:
            return None
    def on_click(self, cell):
        pass


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    board.check()
    # board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
