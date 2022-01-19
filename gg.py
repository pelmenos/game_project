import pygame

pygame.init()

FPS = 15
WIDTH = 660
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(player_sprites, all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 12
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def stand(self):  # нужен чтобы персонаж не застывал во время ходьбы ногой вверх
        self.cur_frame = (self.cur_frame + 1)
        if self.cur_frame == 16:
            self.cur_frame = 12
        elif self.cur_frame == 4:
            self.cur_frame = 0
        elif self.cur_frame == 8:
            self.cur_frame = 4
        elif self.cur_frame == 12:
            self.cur_frame = 8
        self.image = self.frames[self.cur_frame]
        #self.stand_go()

    # def stand_go(self):  # помогает сделать анимацию передвижений более плавной
    #     if self.cur_frame in [0, 1, 2, 3]:
    #         self.rect.y += 25
    #     if self.cur_frame in [4, 5, 6, 7]:
    #         self.rect.x -= 25
    #     if self.cur_frame in [8, 9, 10, 11]:
    #         self.rect.x += 25
    #     if self.cur_frame in [12, 13, 14, 15]:
    #         self.rect.y -= 25

    def go_up(self):  # движение вверх
        if self.cur_frame not in [12, 13, 14, 15]:
            self.cur_frame = 13
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.y -= 25

    def go_down(self):  # движение вниз
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.cur_frame not in [0, 1, 2, 3]:
            self.cur_frame = 1
        self.image = self.frames[self.cur_frame]
        self.rect.y += 25

    def go_left(self):  # движение влево
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.cur_frame not in [4, 5, 6, 7]:
            self.cur_frame = 5
        self.image = self.frames[self.cur_frame]
        self.rect.x -= 25

    def go_right(self):  # движение вправо
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.cur_frame not in [8, 9, 10, 11]:
            self.cur_frame = 9
        self.image = self.frames[self.cur_frame]
        self.rect.x += 25

#
# gg = AnimatedSprite(load_image("red.png", -1), 4, 4, 330 - 64, 250 - 64)
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 gg.go_up()
#             if event.key == pygame.K_DOWN:
#                 gg.go_down()
#             if event.key == pygame.K_LEFT:
#                 gg.go_left()
#             if event.key == pygame.K_RIGHT:
#                 gg.go_right()
#     screen.fill(pygame.Color("black"))
#     all_sprites.draw(screen)
#     pygame.display.flip()
#     if gg.cur_frame % 2 == 1:
#         gg.stand()
#
#     clock.tick(FPS)
#
# pygame.quit()
