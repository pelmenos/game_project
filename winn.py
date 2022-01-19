import pygame
import os
import sys
from Chose_pokemon import PARTNER

size = width, height = 650, 550
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey is not None:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    image = image.convert_alpha()
    return image


class You_win(pygame.sprite.Sprite):
    image = load_image('youwin.png')
    image = pygame.transform.scale(image, (550, 550))

    def __init__(self):
        super().__init__()
        self.image = You_win.image
        self.rect = self.image.get_rect()
        print(self.image.get_width())
        self.rect.x = -self.image.get_width()
        self.fl = True
        self.rect.y = 0

    def update(self):
        if self.fl:
            self.rect.x += 20
            if self.rect.x == 600 - self.image.get_width():
                self.fl = False

    def blitme(self):
        screen.blit(self.image, self.rect)


pygame.init()
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
game = You_win()


def WIN(pers, col):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                WIN2(pers, col)
        screen.fill((0, 0, 0))
        game.blitme()
        game.update()
        pygame.display.flip()
        clock.tick(60)


def WIN2(pers, col):
    txt = f"Вы прошли игру с {pers.name}'om {pers.lvl}-ого левела"
    txt2 = f'Уничтожено монстров: {col}.'
    screen.fill((0, 0, 0))
    dis = 0
    pygame.display.flip()
    for i in txt:
        font = pygame.font.Font(None, 34)
        text = font.render(i, True, (0, 255, 0))
        screen.blit(text, (25 + dis, 100))
        dis += 12
        pygame.display.flip()
    dis = 0
    for i in txt2:
        font = pygame.font.Font(None, 34)
        text = font.render(i, True, (0, 255, 0))
        screen.blit(text, (25 + dis, 150))
        dis += 12
        pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
