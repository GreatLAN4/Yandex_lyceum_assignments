import pygame



def draw(screen):
    screen.fill((0, 0, 255))
    small_side = side / number
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if i % 2 != 0:
                screen.fill(pygame.Color('black'), (side - small_side * j, side - small_side * i, small_side, small_side))
            elif i % 2 == 0:
                screen.fill(pygame.Color('white'), (side - small_side * j, side - small_side * i, small_side, small_side))

    # left, top, width, height = [small_side] * 4
    # for i in range(number):
    #     left, top, width, height = [side - small_side] * 4
    #     white_square = pygame.Rect(left, top, width, height)
    #     screen.fill(pygame.Color('white'), white_square)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Шахматная клетка")

    side, number = "500", "10"# input(), input()

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
