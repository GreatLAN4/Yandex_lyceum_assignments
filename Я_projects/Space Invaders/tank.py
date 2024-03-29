import pygame


# code for tank working
class Tank:

    def __init__(self, screen, FPS):
        # tank initialization == game character
        self.FPS = FPS
        self.screen = screen
        self.pic = pygame.image.load("data/tank.png")
        self.rect = self.pic.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright, self.mleft = False, False

    def Output(self):
        # Drawing and output of the tank
        self.screen.blit(self.pic, self.rect)

    def Update(self):
        # updating tank's position
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += (140 / self.FPS)

        elif self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= (140 / self.FPS)

        self.rect.centerx = self.center

    def TankSpawn(self):
        # Spawns tank in the middle of the screen in the bottom
        self.center = self.screen_rect.centerx
