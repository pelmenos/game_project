import pygame
import os
import sys


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


class Game_over(pygame.sprite.Sprite):
    image = load_image('gameover.jpg')
    image = pygame.transform.scale(image, (550, 550))

    def __init__(self):
        super().__init__()
        self.image = Game_over.image
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
game = Game_over()


def END(col):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        game.blitme()
        game.update()
        if not game.fl:
            font = pygame.font.Font(None, 34)
            text = font.render(f'Уничтожено монстров: {col}. И всё равно не добрались...', True, (0, 255, 0))
            screen.blit(text, (25, 400))
        pygame.display.flip()
        clock.tick(60)
