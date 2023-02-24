import pygame
import math
import random


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = pygame.Color("white")
        self.speed = 100
        self.direction = random.uniform(math.pi / 4, 3 * math.pi / 4)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, dt, screen_width, screen_height):
        dx = self.speed * -math.sin(self.direction) * dt
        dy = self.speed * -math.sin(self.direction) * dt
        self.x += dx
        self.y += dy

        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.direction = math.pi - self.direction
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.direction = -self.direction


pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")

balls = []

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ball = Ball(*event.pos)
            balls.append(ball)

    dt = clock.tick(60) / 1000
    for ball in balls:
        ball.update(dt, screen_width, screen_height)

    screen.fill(pygame.Color("black"))
    for ball in balls:
        ball.draw(screen)

    pygame.display.update()

pygame.quit()
