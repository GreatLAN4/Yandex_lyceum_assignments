import pygame


def draw(screen):
    screen.fill(pygame.Color('red'), (1, 1, width - 2, height - 2))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Прямоугольник")
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
    exit()
