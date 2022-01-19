import sys
import pygame
import pygame_gui
from Chose_pokemon import PARTNER
from random import randint
import time
from endd import END


def terminate():
    pygame.quit()
    sys.exit()


def create_text(size, txt, x, y):  # для создания надписей
    font = pygame.font.Font(None, size)
    text = font.render(txt, True, (0, 0, 0))
    screen.blit(text, (x, y))


def create_rect(enemy):  # создаёт прямоугольники со шкалой здоровья и опытом
    pygame.draw.rect(screen, (0, 0, 0), ((400, 280), (205, 90)), 2)
    pygame.draw.line(screen, pygame.Color('green'), (405, 325), (405 + len_hp_scale_my, 325), 20)
    pygame.draw.line(screen, pygame.Color('blue'), (405, 355), (400 + PARTNER.exp * 2, 355), 5)
    create_text(24, PARTNER.name, 405, 285)
    create_text(24, 'lvl ' + str(PARTNER.lvl), 560, 285)
    create_text(16, 'hp:', 405, 305)
    create_text(16, 'exp:', 405, 340)

    pygame.draw.rect(screen, (0, 0, 0), ((25, 75), (205, 90)), 2)
    create_text(24, enemy.name, 30, 80)
    create_text(24, 'lvl ' + str(enemy.lvl), 185, 80)
    create_text(16, 'hp:', 30, 100)
    pygame.draw.line(screen, pygame.Color('green'), (30, 120), (30 + len_hp_scale_enemy, 120), 20)
    create_text(16, 'exp:', 30, 135)
    pygame.draw.line(screen, pygame.Color('blue'), (30, 150), (25 + enemy.exp * 2, 150), 5)


def anim_start(enemy):
    if PARTNER.rect.x != 50:
        PARTNER.rect.x += 5
        PARTNER.rect.y = 180
    if not lose:
        PARTNER.blitme()
    if enemy.rect.x != 350:
        enemy.rect.x -= 5
    if not win:
        enemy.blitme()


def col_dmg(scale, pers_take, pers_give,
            num):  # рассчитываетсяч наносимый урон способности или понижение стата. возвращает сколько отнять от рисумой полоски хп
    global win, lose, kill
    if pers_give.ability[num].distance == 'phy':
        damage = (pers_give.ability[num].dmg * (1 + pers_give.attack / 100) - pers_take.defence) / 2
    elif pers_give.ability[num].distance == 'spec':
        damage = (pers_give.ability[num].dmg * (1 + pers_give.special_attack / 100) - pers_take.special_defence) / 2
    else:
        if pers_give.ability[num].type == 'defence':
            pers_take.defence *= pers_give.ability[num].dmg
            return 0
        elif pers_give.ability[num].type == 'attack':
            pers_take.attack *= pers_give.ability[num].dmg
            return 0
    if damage < 0:
        return 1
    if damage < pers_take.hp:
        proc = damage / pers_take.all_hp * 100
        pers_take.hp -= damage
        return scale / 100 * proc
    else:
        if pers_take == PARTNER:
            lose = True
        else:
            win = True
            kill += 1
        return 1000


def end(enemy):
    global win, lose, the_end
    if win:
        drawing(enemy)
        dis = 0
        a = f"{enemy.name} can't continue."
        b = f"{PARTNER.name} gained {enemy.all_hp} exp."
        PARTNER.exp += enemy.all_hp * 2
        for j, i in enumerate(a):
            create_text(20, i, 25 + dis, 400)
            pygame.display.flip()
            dis += 8
            time.sleep(0.08)
        dis = 0
        for j, i in enumerate(b):
            create_text(20, i, 25 + dis, 410)
            pygame.display.flip()
            dis += 8
            time.sleep(0.08)
        the_end = True
    elif lose:
        drawing(enemy)
        dis = 0
        a = f"{PARTNER.name} can't continue."
        b = f"Your adventure is ending here."
        for j, i in enumerate(a):
            create_text(20, i, 25 + dis, 400)
            pygame.display.flip()
            dis += 8
            time.sleep(0.08)
        dis = 0
        for j, i in enumerate(b):
            create_text(20, i, 25 + dis, 410)
            pygame.display.flip()
            dis += 8
            time.sleep(0.08)
        END(kill)


def drawing(enemy):  # рисует весь интерфейс
    screen.fill(pygame.Color('white'))
    pygame.draw.rect(screen, (0, 0, 0), ((15, 390), (620, 110)), width=5)
    pygame.draw.rect(screen, (0, 0, 0), ((15, 390), (333, 110)), width=5)
    create_rect(enemy)
    anim_start(enemy)
    manager.draw_ui(screen)
    pygame.display.flip()


def balt(num, pers):  # перед применением способности показывает на панеле, кто что использует
    dis = 0
    a = f'{pers.name} use {pers.ability[num].name}'
    for j, i in enumerate(a):
        create_text(20, i, 25 + dis, 400)
        pygame.display.flip()
        dis += 8
        time.sleep(0.08)


pygame.init()

size = 650, 550
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Битва')

manager = pygame_gui.UIManager((650, 550))
clock = pygame.time.Clock()

win = False
lose = False
the_end = False
kill = 0
len_hp_scale_enemy = 195
len_hp_scale_my = 195

btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((377, 400), (110, 40)),
    text=PARTNER.ability[0].name,
    manager=manager)
btn2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((497, 400), (110, 40)),
    text=PARTNER.ability[1].name,
    manager=manager)

btn3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((377, 450), (110, 40)),
    text=PARTNER.ability[2].name,
    manager=manager)

btn4 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((497, 450), (110, 40)),
    text=PARTNER.ability[3].name,
    manager=manager)


def Battle(enemy):
    global len_hp_scale_enemy, len_hp_scale_my, win, lose, the_end, kill
    len_hp_scale_enemy = 195
    if PARTNER.all_hp == PARTNER.hp:
        len_hp_scale_my = 195
    win = False
    lose = False
    the_end = False
    PARTNER.rect.x, PARTNER.rect.y = -200, 175
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                num_enemy = randint(0, 3)
                if event.ui_element == btn:
                    if PARTNER.speed >= enemy.speed:
                        len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 0)
                        balt(0, PARTNER)
                        if len_hp_scale_enemy < 0:
                            len_hp_scale_enemy = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(num_enemy, enemy)
                            len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                            if len_hp_scale_my < 0:
                                len_hp_scale_my = 0
                                end(enemy)
                    else:
                        len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                        balt(num_enemy, enemy)
                        if len_hp_scale_my < 0:
                            len_hp_scale_my = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(0, PARTNER)
                            len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 0)
                            if len_hp_scale_enemy < 0:
                                len_hp_scale_enemy = 0
                                end(enemy)
                elif event.ui_element == btn2:
                    if PARTNER.speed >= enemy.speed:
                        len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 1)
                        balt(1, PARTNER)
                        if len_hp_scale_enemy < 0:
                            len_hp_scale_enemy = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(num_enemy, enemy)
                            len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                            if len_hp_scale_my < 0:
                                len_hp_scale_my = 0
                                end(enemy)
                    else:
                        len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                        balt(num_enemy, enemy)
                        if len_hp_scale_my < 0:
                            len_hp_scale_my = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(1, PARTNER)
                            len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 1)
                            if len_hp_scale_enemy < 0:
                                len_hp_scale_enemy = 0
                                end(enemy)
                elif event.ui_element == btn3:
                    if PARTNER.speed >= enemy.speed:
                        len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 2)
                        balt(2, PARTNER)
                        if len_hp_scale_enemy < 0:
                            len_hp_scale_enemy = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(num_enemy, enemy)
                            len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                            if len_hp_scale_my < 0:
                                len_hp_scale_my = 0
                                end(enemy)
                    else:
                        len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                        balt(num_enemy, enemy)
                        if len_hp_scale_my < 0:
                            len_hp_scale_my = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(2, PARTNER)
                            len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 2)
                            if len_hp_scale_enemy < 0:
                                len_hp_scale_enemy = 0
                                end(enemy)
                elif event.ui_element == btn4:
                    if PARTNER.speed >= enemy.speed:
                        len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 3)
                        balt(3, PARTNER)
                        if len_hp_scale_enemy < 0:
                            len_hp_scale_enemy = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(num_enemy, enemy)
                            len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                            if len_hp_scale_my < 0:
                                len_hp_scale_my = 0
                                end(enemy)
                    else:
                        len_hp_scale_my -= col_dmg(195, PARTNER, enemy, num_enemy)
                        balt(num_enemy, enemy)
                        if len_hp_scale_my < 0:
                            len_hp_scale_my = 0
                            drawing(enemy)
                            end(enemy)
                        else:
                            drawing(enemy)
                            time.sleep(0.5)
                            balt(3, PARTNER)
                            len_hp_scale_enemy -= col_dmg(195, enemy, PARTNER, 3)
                            if len_hp_scale_enemy < 0:
                                len_hp_scale_enemy = 0
                                end(enemy)
                if the_end:
                    return
            manager.process_events(event)
        manager.update(time_delta)

        drawing(enemy)
