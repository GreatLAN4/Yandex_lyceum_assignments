import pygame
import math


class GameCharacter:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)
        self.speed = 0.05
        self.target_x = None
        self.target_y = None

    def move_towards(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

    def update(self):
        if self.target_x is not None and self.target_y is not None:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > self.speed:
                self.x += dx / distance * self.speed
                self.y += dy / distance * self.speed
            else:
                self.x = self.target_x
                self.y = self.target_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


pygame.init()

screen_width = 501
screen_height = 501
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Character")

game_character = GameCharacter(screen_width / 2, screen_height / 2, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_character.move_towards(event.pos[0], event.pos[1])

    screen.fill((255, 255, 255))
    game_character.update()
    game_character.draw(screen)
    pygame.display.flip()

pygame.quit()
