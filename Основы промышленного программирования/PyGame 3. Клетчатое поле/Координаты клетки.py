import pygame


class Board:
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
        board_width = self.width * self.cell_size
        board_height = self.height * self.cell_size
        if self.left < mouse_pos[0] < self.left + board_width:
            if self.top < mouse_pos[1] < self.top + board_height:
                cell_coords = (mouse_pos[1] - self.left) // self.cell_size, \
                              (mouse_pos[0] - self.top) // self.cell_size
                return cell_coords
        return None

    def on_click(self, cell_coords):
        i = cell_coords[0] // 50 - self.left // 50
        j = cell_coords[1] // 50 - self.top // 50
        if (i >= 0 and j >= 0) and (i < self.width and j < self.height):
            i = cell_coords[0] // 50 - self.left // 50
            j = cell_coords[1] // 50 - self.top // 50
            print((i, j))
        else:
            print(None)


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    board.check()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
