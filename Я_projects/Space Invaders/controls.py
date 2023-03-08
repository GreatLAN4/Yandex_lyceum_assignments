import pygame
import sys
from bullet import Bullet
from invader import Invader
from time import sleep

# container py file for all events
def events(screen, tank, bullet):
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                # right
                tank.mright = True

            elif event.key == pygame.K_a:
                # left
                tank.mleft = True

            elif event.key == pygame.K_SPACE:
                # space
                new_bullet = Bullet(screen, tank)
                bullet.add(new_bullet)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                # right
                tank.mright = False

            elif event.key == pygame.K_a:
                # left
                tank.mleft = False


def UpdateScreen(bg_color, screen, tank, invaders, bullets):
    # Screen updating
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.DrawBullet()
    invaders.draw(screen)
    tank.Output()

    pygame.display.flip()


def UpdateBullets(invaders, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collections = pygame.sprite.groupcollide(bullets, invaders, True, True)

def TankWaste(stats, screen, tank, invaders, bullets):
    stats.HitPoints -= 1
    invaders.empty()
    bullets.empty()
    CreateArmy(screen, invaders)
    tank.TankSpawn()
    sleep(3)

def UpdateInvaders(stats, screen, tank, invaders, bullets):
    invaders.update()
    if pygame.sprite.spritecollideany(tank, invaders):
        TankWaste(stats, screen, tank, invaders, bullets)


def CreateArmy(screen, invaders):
    invader = Invader(screen)
    inv_width = invader.rect.width
    inv_height = invader.rect.height
    n_inv_x = int((600 - 2 * inv_width) / inv_width)
    n_inv_y = int((640 - 50 - 2 * inv_height) / inv_height)

    for row in range(n_inv_y - 7):
        for inv_n in range(n_inv_x):
            invader = Invader(screen)
            invader.x = inv_width + (inv_width * inv_n)
            invader.y = inv_height + (inv_height * row)

            invader.rect.x = invader.x
            invader.rect.y = invader.rect.height + invader.rect.height * row
            invaders.add(invader)
