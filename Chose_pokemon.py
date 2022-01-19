import pygame
from bulbasaur import Bulbasaur, Bulbasaur_back
from charmander import Charmander, Charmander_back
from squirtle import Squirtle, Squirtle_back


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 10)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        return self.get_cell(mouse_pos)

    def get_cell(self, mouse_pos):
        if self.left < int(mouse_pos[0]) < self.cell_size * self.width + self.left and self.top < int(
                mouse_pos[1]) < self.cell_size * self.height + self.top:
            for i in range(1, self.height + 1):
                for j in range(1, self.width + 1):
                    if self.left + (j - 1) * self.cell_size <= int(mouse_pos[0]) <= self.left + j * self.cell_size \
                            and self.cell_size * (i - 1) + self.top <= int(
                        mouse_pos[1]) <= self.cell_size * i + self.top:
                        return j - 1, i - 1
        else:
            return None


monster_sprite = pygame.sprite.Group()
Bulbasaur = Bulbasaur(monster_sprite, -10, 150)
Squirtle = Squirtle(monster_sprite, 190, 140)
Charmander = Charmander(monster_sprite, 390, 140)

pygame.init()
size = 650, 550
PARTNER = ''
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Выбор твоего партнёра')

board = Board(3, 1)
board.set_view(325 - 300, 275 - 100, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            a = board.get_click(event.pos)
            if a:
                if a == (0, 0):
                    PARTNER = Bulbasaur_back(-200, 175)
                elif a == (1, 0):
                    PARTNER = Squirtle_back(-200, 175)
                elif a == (2, 0):
                    PARTNER = Charmander_back(-200, 175)
                running = False
    screen.fill((255, 255, 255))
    monster_sprite.draw(screen)
    board.render(screen)
    pygame.display.flip()
