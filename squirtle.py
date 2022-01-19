import pygame
import os
from Moves import Tackle, Leer, Water_gun, Shell_spin

size = width, height = 650, 550
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Squirtle(pygame.sprite.Sprite):
    bulb = load_image('squirtle.png')
    bulb = pygame.transform.scale(bulb, (288, 288))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Squirtle.bulb
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        screen.blit(self.image, self.rect)


class Squirtle_back(pygame.sprite.Sprite):
    bulb = load_image('squirtle_back.png')
    bulb = pygame.transform.scale(bulb, (288, 288))

    def __init__(self, x, y):
        super().__init__()
        self.name = 'Squirtle'
        self.image = Squirtle_back.bulb
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lvl = 1
        self.hp = 44
        self.all_hp = 44
        self.attack = 48
        self.defence = 65
        self.special_attack = 50
        self.special_defence = 64
        self.speed = 43
        self.exp = 0
        self.add_stat = {'hp': +6, 'attack': +3, 'defence': +6, 'special_attack': +3, 'special_defence': +3, 'speed': + 3}
        self.ability = [Tackle(), Leer(), Shell_spin(), Water_gun()]

    def blitme(self):
        screen.blit(self.image, self.rect)

    def re_exp(self):
        if self.exp >= 100:
            self.lvl += 1
            self.all_hp += self.add_stat['hp']
            self.hp = self.all_hp
            self.attack += self.add_stat['attack']
            self.defence += self.add_stat['defence']
            self.special_attack += self.add_stat['special_attack']
            self.special_defence += self.add_stat['special_defence']
            self.speed += self.add_stat['speed']
            self.exp = self.exp % 100
