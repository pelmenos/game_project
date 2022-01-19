import os
import pygame
from Moves import Tackle, Scratch, Growl, Leer, Razor_leaf

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


class Rattata():
    bulb_back = load_image('rattata.png')
    bulb_back = pygame.transform.scale(bulb_back, (288, 288))

    def __init__(self, lvl, x=800, y=0):
        super().__init__()
        self.name = 'Rattata'
        self.image = Rattata.bulb_back
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stat = [28, 56, 35, 25, 34, 72]
        self.add_stat = {'hp': +2, 'attack': +1, 'defence': +1, 'special_attack': +2, 'special_defence': +1, 'speed': + 1}
        self.lvl = lvl
        self.all_hp = 28 + self.add_stat['hp'] * self.lvl
        self.hp = self.stat[0] + self.add_stat['hp'] * self.lvl
        self.attack = self.stat[1] + self.add_stat['attack'] * self.lvl
        self.defence = self.stat[2] + self.add_stat['defence'] * self.lvl
        self.special_attack = self.stat[3] + self.add_stat['special_attack'] * self.lvl
        self.special_defence = self.stat[4] + self.add_stat['special_defence'] * self.lvl
        self.speed = self.stat[5] + self.add_stat['speed'] * self.lvl
        self.exp = 1
        self.ability = [Tackle(), Growl(), Scratch(), Leer()]

    def blitme(self):
        screen.blit(self.image, self.rect)


class Geodude():
    bulb_back = load_image('geodude.png')
    bulb_back = pygame.transform.scale(bulb_back, (288, 288))

    def __init__(self, lvl, x=800, y=0):
        super().__init__()
        self.name = 'Geodude'
        self.image = Geodude.bulb_back
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stat = [39, 60, 90, 30, 30, 20]
        self.add_stat = {'hp': +1, 'attack': +1, 'defence': +3, 'special_attack': +1, 'special_defence': +2, 'speed': + 1}
        self.lvl = lvl
        self.all_hp = 39 + self.add_stat['hp'] * self.lvl
        self.hp = self.stat[0] + self.add_stat['hp'] * self.lvl
        self.attack = self.stat[1] + self.add_stat['attack'] * self.lvl
        self.defence = self.stat[2] + self.add_stat['defence'] * self.lvl
        self.special_attack = self.stat[3] + self.add_stat['special_attack'] * self.lvl
        self.special_defence = self.stat[4] + self.add_stat['special_defence'] * self.lvl
        self.speed = self.stat[5] + self.add_stat['speed'] * self.lvl
        self.exp = 1
        self.ability = [Tackle(), Tackle(), Tackle(), Leer()]

    def blitme(self):
        screen.blit(self.image, self.rect)


class Oddish():
    bulb_back = load_image('oddish.png')
    bulb_back = pygame.transform.scale(bulb_back, (288, 288))

    def __init__(self, lvl, x=800, y=0):
        super().__init__()
        self.name = 'Oddish'
        self.image = Oddish.bulb_back
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stat = [35, 50, 45, 65, 55, 30]
        self.add_stat = {'hp': +1, 'attack': +1, 'defence': +2, 'special_attack': +2, 'special_defence': +2, 'speed': + 1}
        self.lvl = lvl
        self.all_hp = 35 + self.add_stat['hp'] * self.lvl
        self.hp = self.stat[0] + self.add_stat['hp'] * self.lvl
        self.attack = self.stat[1] + self.add_stat['attack'] * self.lvl
        self.defence = self.stat[2] + self.add_stat['defence'] * self.lvl
        self.special_attack = self.stat[3] + self.add_stat['special_attack'] * self.lvl
        self.special_defence = self.stat[4] + self.add_stat['special_defence'] * self.lvl
        self.speed = self.stat[5] + self.add_stat['speed'] * self.lvl
        self.exp = 1
        self.ability = [Tackle(), Tackle(), Razor_leaf(), Leer()]

    def blitme(self):
        screen.blit(self.image, self.rect)

