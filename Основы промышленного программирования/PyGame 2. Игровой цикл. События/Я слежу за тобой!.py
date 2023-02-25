import pygame

screen_width, screen_height = 200, 200


def draw(screen, n):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render(str(n), True, "red")
    text_x = screen_width // 2 - text.get_width() // 2
    text_y = screen_height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def main():
    pygame.init()

    n = 0
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Draggable Square")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWMINIMIZED:
                n += 1
        draw(screen, n)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
