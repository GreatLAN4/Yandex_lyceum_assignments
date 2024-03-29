import pygame
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, tank, FPS):
        # adding bullet with tanks pos.
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 12)
        self.color = "white"
        self.speed = 45 / FPS
        self.rect.centerx = tank.rect.centerx
        self.rect.top = tank.rect.top
        self.y = float(self.rect.y)


    def update(self):
        # Bullet's movings
        self.y -= self.speed
        self.rect.y = self.y

    def DrawBullet(self):
        # Draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)


