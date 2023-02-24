    import pygame


    class Square:
        def __init__(self, size, x, y, color):
            self.size = size
            self.rect = pygame.Rect(x, y, size, size)
            self.color = color
            self.offset_x = 0
            self.offset_y = 0
            self.dragging = False

        def draw(self, surface):
            pygame.draw.rect(surface, self.color, self.rect)

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    self.dragging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.rect.x - mouse_x
                    self.offset_y = self.rect.y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    mouse_x, mouse_y = event.pos
                    self.rect.x = mouse_x + self.offset_x
                    self.rect.y = mouse_y + self.offset_y


    def main():

        pygame.init()

        screen_width, screen_height = 300, 300
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Draggable Square")

        square_size = 100
        square_color = pygame.Color("green")
        square = Square(square_size, 0, 0, square_color)
        square.rect.center = (screen_width // 2, screen_height // 2)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    square.handle_event(event)

            screen.fill(pygame.Color("black"))
            square.draw(screen)

            pygame.display.update()

        pygame.quit()

    if __name__ == "__main__":
        main()
