import pygame
import setting as s
import func_back as fb
import race as r
import player as p
import spec as sp
import pole_gener as pg
import game_back as gb
import sound_sets as ss
import time

pygame.init()

scale = 5
ramp = 40
shag = 20
chat = []


def chat_gener(ch):
    for i in range(ramp+1):
        ch.append(' ')


def chat_check(screen, nx, ny, y, chat, put):
    tim = time.strftime("%H:%M:%S")
    if pg.a[ny+y*2 + 2][nx] == '1':
        t = tim + '  ' + 'Вы нашли ' + str(put) + ' золотых'
        chat_update(chat, t)
        chat_print(chat, screen)
    if pg.a[ny+y*3 + 3][nx] == '1':
        p.enemy_hello += 1
        t = tim + '  ' + 'Вы встретили ' + str(p.enemy_hello) + '-ого врага !'
        chat_update(chat, t)
        chat_print(chat, screen)


def chat_update(ch, new):
    for i in range(ramp):
        ch[ramp - i] = ch[ramp - i - 1]
    ch[0] = new


def chat_print(ch, screen):
    f = pygame.font.Font(None, 20)
    start = 10
    color = s.white
    for i in range(scale):
        put = f.render(str(ch[i]), 1, color)
        screen.blit(put, (start, s.scr_y-20-i*shag))


def chat_all_print(ch, screen):
    f = pygame.font.Font(None, 20)
    start = 10
    color = s.white
    for i in range(ramp):
        put = f.render(str(ch[i]), 1, color)
        screen.blit(put, (start, s.scr_y-20-i*shag))
