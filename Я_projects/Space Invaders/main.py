import controls
import pygame
import sys
from pygame.sprite import Group
from tank import Tank
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 640))
    pygame.display.set_caption("space invaders")
    bg_color = (0, 0, 0)
    tank = Tank(screen)
    bullets = Group()
    invaders = Group()
    controls.CreateArmy(screen, invaders)
    stats = Stats()

    while True:
        controls.events(screen, tank, bullets)
        tank.Update()
        controls.UpdateScreen(bg_color, screen, tank, invaders, bullets)
        controls.UpdateBullets(invaders, bullets)
        controls.UpdateInvaders(stats, screen, tank, invaders, bullets)


run()
