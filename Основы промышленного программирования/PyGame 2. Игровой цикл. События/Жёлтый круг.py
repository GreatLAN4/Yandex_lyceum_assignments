import pygame


def draw(screen, flag, x=0, y=0, ):
    if flag:
        pygame.draw.circle(screen, "yellow", (x, y), radius)
    else:
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running, expand = True, False
    radius, x, y = 0, 0, 0
    v = 20
    fps = 120
    screen.fill("blue")

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill("blue")
                x, y = mouse_x, mouse_y
                radius = 0
                expand = True

        draw(screen, expand, x, y)

        pygame.display.flip()
        radius += v / fps
        clock.tick(fps)

    pygame.quit()
