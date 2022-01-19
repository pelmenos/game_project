import os
import sys
import pygame
from gg import AnimatedSprite, all_sprites, player_sprites
from Battle_theme import Battle, PARTNER, kill
from Enemies import Rattata, Geodude, Oddish
from random import randint
from winn import WIN

pygame.init()

FPS = 10
WIDTH = 650
HEIGHT = 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = None
tiles_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
bush_group = pygame.sprite.Group()
end_group = pygame.sprite.Group()


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


def load_level(filename):
    filename = "data\\" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = AnimatedSprite(load_image("red.png", -1), 4, 4, x * 50, y * 50)
    return new_player, x, y


def generate_level_2_layer(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile_tree('wall', x, y)
            elif level[y][x] == '*':
                Tile_bush('bush', x, y)
            elif level[y][x] == '0':
                Tile_end('end', x, y)


class Camera:
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


def terminate():
    pygame.quit()
    sys.exit()


tile_images = {'wall': pygame.transform.scale(load_image('tree.png', -1), (50, 50)),
               'empty': pygame.transform.scale(load_image('grass.png'), (50, 50)),
               'bush': pygame.transform.scale(load_image('bush.png', -1), (60, 60)),
               'end': pygame.transform.scale(load_image('end.png', -1), (100, 100))}

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Tile_tree(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tree_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Tile_bush(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(bush_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Tile_end(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(end_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


def lvl_cap(pers):#для подбора уровня противнику
    if pers == 1 or pers == 2:
        return pers
    else:
        return randint(pers - 2, pers + 1)


player, level_x, level_y = generate_level(load_level('map.txt'))#загрузка слоя травы
ending = generate_level_2_layer(load_level('map2.txt'))#загрузка всех перпятствий с которыми будет происходить столкновение(кусты, деревья# )
camera = Camera((level_x, level_y))

running = True

while running:
    fl = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
                if pygame.sprite.spritecollide(player, tree_group, False):
                    player.go_right()
                    player.go_right()
                    player.go_left()

            if event.key == pygame.K_RIGHT:
                player.go_right()
                if pygame.sprite.spritecollide(player, tree_group, False):
                    player.go_left()
                    player.go_left()
                    player.go_right()

            if event.key == pygame.K_UP:
                player.go_up()
                if pygame.sprite.spritecollide(player, tree_group, False):
                    player.go_down()
                    player.go_down()
                    player.go_up()

            if event.key == pygame.K_DOWN:
                player.go_down()
                if pygame.sprite.spritecollide(player, tree_group, False):
                    player.go_up()
                    player.go_up()
                    player.go_down()

            if pygame.sprite.spritecollide(player, bush_group, False) and randint(0, 9) in [1, 2]:
                random_enemy = randint(0, 2)
                if random_enemy == 0:
                    Battle(Rattata(lvl_cap(PARTNER.lvl)))
                elif random_enemy == 1:
                    Battle(Geodude(lvl_cap(PARTNER.lvl)))
                else:
                    Battle(Oddish(PARTNER.lvl))
                PARTNER.re_exp()

            if pygame.sprite.spritecollide(player, end_group, False):
                WIN(PARTNER, kill)


    camera.update(player)

    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill(pygame.Color(250, 0, 0))
    tiles_group.draw(screen)
    tree_group.draw(screen)
    bush_group.draw(screen)
    end_group.draw(screen)
    player_sprites.draw(screen)
    pygame.display.flip()
    if player.cur_frame % 2 == 1:
        player.stand()
    clock.tick(FPS)

terminate()
