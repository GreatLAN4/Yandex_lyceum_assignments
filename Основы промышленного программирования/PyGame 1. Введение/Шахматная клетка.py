import pygame


def draw(screen):
    screen.fill((0, 0, 255))
    small_side = side / number
    edge = (small_side, small_side)
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if j % 2 == 0:
                if i % 2 != 0:
                    screen.fill(pygame.Color('black'), (side - small_side * j, side - small_side * i, *edge))
                elif i % 2 == 0:
                    screen.fill(pygame.Color('white'), (side - small_side * j, side - small_side * i, *edge))
            else:
                if i % 2 != 0:
                    screen.fill(pygame.Color('white'), (side - small_side * j, side - small_side * i, *edge))
                elif i % 2 == 0:
                    screen.fill(pygame.Color('black'), (side - small_side * j, side - small_side * i, *edge))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Шахматная клетка")

    side, number = input(), input()

    if side.isdigit() and number.isdigit():
        size, side, number = (int(side), int(side)), int(side), int(number)
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
