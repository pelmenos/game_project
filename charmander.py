import pygame
import os
from Moves import Scratch, Leer, Ember, Fire_punch


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


class Charmander(pygame.sprite.Sprite):
    bulb = load_image('charmander.png')
    bulb = pygame.transform.scale(bulb, (288, 288))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Charmander.bulb
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Charmander_back(pygame.sprite.Sprite):
    bulb = load_image('charmander_back.png')
    bulb = pygame.transform.scale(bulb, (288, 288))

    def __init__(self, x, y):
        super().__init__()
        self.name = 'Charmander'
        self.image = Charmander_back.bulb
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lvl = 1
        self.hp = 39
        self.all_hp = 39
        self.attack = 52
        self.defence = 43
        self.special_attack = 60
        self.special_defence = 50
        self.speed = 65
        self.exp = 0
        self.add_stat = {'hp': +6, 'attack': +6, 'defence': +3, 'special_attack': +3, 'special_defence': +3, 'speed': + 3}
        self.exp_cap = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
        self.ability = [Scratch(), Leer(), Fire_punch(), Ember()]

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
