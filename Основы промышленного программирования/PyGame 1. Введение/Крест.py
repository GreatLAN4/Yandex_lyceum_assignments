import pygame


def draw(screen):
    pygame.draw.line(screen, "white", (0, 0), (width, height), 5)
    pygame.draw.line(screen, "white", (0, height), (width, 0), 5)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Крест")
    width, height = input(), input()

    if width.isdigit() and height.isdigit():
        size, width, height = (int(width), int(height)), int(width), int(height)
    else:
        print("Неправильный формат ввода")
        exit()

    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
