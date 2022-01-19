import pygame, sys, random
from pygame.locals import *

DIRECTION = {pygame.K_a: (-1, 0),
             pygame.K_d: (1, 0),
             pygame.K_w: (0, -1),
             pygame.K_s: (0, 1)}

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
screen_rect = windowSurface.get_rect()
pygame.display.set_caption('skjutare')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player:
    playersize_x = 50
    playersize_y = 50
    speed = 6
    player_RECT = pygame.Rect(300, 100, playersize_x, playersize_y)
    HP = 20


class Bullet:
    bulletsize_x = 10
    bulletsize_y = 10
    speed = 12

    def __init__(self, player):
        self.bullet_RECT = bullet_RECT = pygame.Rect(player.player_RECT.left,
                                                     player.player_RECT.top,
                                                     Bullet.bulletsize_x,
                                                     Bullet.bulletsize_y)


bullets = []
enemies = []

# spel-loopen
while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == ord(" "):
                bullets.append(Bullet)

    for key in DIRECTION:
        if keys[key]:
            Player.player_RECT.x += DIRECTION[key][0] * Player.speed
            Player.player_RECT.y += DIRECTION[key][1] * Player.speed

    Player.player_RECT.clamp_ip(screen_rect)  # håller spelaren på skrämen

    windowSurface.fill(BLACK)

    for Bullet in bullets:
        Bullet.bullet_RECT.top -= Bullet.speed

        pygame.draw.rect(windowSurface, WHITE, Bullet.bullet_RECT)

    bullets = [bullet for bullet in bullets if bullet.bullet_RECT.top >= 0]

    pygame.draw.rect(windowSurface, GREEN, Player.player_RECT)

    pygame.display.update()
    mainClock.tick(40)
