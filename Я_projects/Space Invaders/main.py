import controls
import pygame
import sys
from pygame.sprite import Group
from tank import Tank
from stats import Stats
from score import Scores

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
    score = Scores(screen, stats)

    while True:
        controls.events(screen, tank, bullets)
        if stats.game_run:
            tank.Update()
            controls.UpdateScreen(bg_color, screen, stats, score, tank, invaders, bullets)
            controls.UpdateBullets(screen, invaders, bullets)
            controls.UpdateInvaders(stats, screen, tank, invaders, bullets)


run()
