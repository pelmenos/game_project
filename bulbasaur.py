import pygame
import os
from Moves import Tackle, Growl, Razor_leaf, Vine_whip

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


class Bulbasaur(pygame.sprite.Sprite):
    bulb = load_image('bulbasaur.png')
    bulb = pygame.transform.scale(bulb, (288, 288))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bulbasaur.bulb
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Bulbasaur_back(pygame.sprite.Sprite):
    bulb_back = load_image('bulbasaur_back.png')
    bulb_back = pygame.transform.scale(bulb_back, (288, 288))

    def __init__(self, x, y):
        super().__init__()
        self.name = 'Bulbasaur'
        self.image = Bulbasaur_back.bulb_back
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lvl = 1
        self.hp = 45
        self.all_hp = 45
        self.attack = 49
        self.defence = 49
        self.special_attack = 65
        self.special_defence = 65
        self.speed = 45
        self.exp = 0
        self.add_stat = {'hp': +6, 'attack': +3, 'defence': +3, 'special_attack': +6, 'special_defence': +3, 'speed': + 3}
        self.ability = [Tackle(), Growl(), Vine_whip(), Razor_leaf()]

    def blitme(self):
        screen.blit(self.image, self.rect)

    def re_exp(self):#повышение уровня
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
