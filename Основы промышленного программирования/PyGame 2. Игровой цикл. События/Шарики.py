from random import randint

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 750, 750
TIMER_EVENT = 30
FPS = 120


class MovingCircle:

    def __init__(self):
        global FPS
        self.v = 100
        self.r = 10

    def Render(self, screen, pos):
        pygame.draw.circle(screen, "white", (pos[0], pos[1]), 10)

    def Move(self, pos):
        self.x = pos[0] + self.v / FPS
        self.y = pos[1] + self.v / FPS


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    movingcircle = MovingCircle()
    screen.fill((0, 0, 0))
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                movingcircle.Render(screen, event.pos)

        pygame.display.flip()
    pygame.display.quit()


if __name__ == "__main__":
    main()
