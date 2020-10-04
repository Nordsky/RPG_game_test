import pygame
import setting as s
import player as p
import monster as mo
import pole_gener as pg
import random

spell_move = True
monster = pygame.image.load(mo.all_monst[0])
hp = pygame.image.load('pic/icon/bat_hp_1.png')
mana = pygame.image.load('pic/icon/bat_mana_1.png')
defen = pygame.image.load('pic/icon/bat_def_1.png')

race = p.player_race(p.player_lvl)
spec = p.player_spec(p.player_lvl)


def random_enemy():
    global monster
    ch = random.randint(0, 4)
    monster = pygame.image.load(mo.all_monst[ch])


# spell info XD
def spell_info(screen, pan):
    f = pygame.font.Font(None, 28)
    g = pygame.font.Font(None, 25)
    color = s.cyan
    n = []
    flag = True
    # s.show_button(screen, s.scr_x / 2 - 150, 20, 300, 300)
    # s.show_button(screen, s.scr_x / 2 + 130, 20, 20, 20)

    if pan == "skill_1_1":
        sk_name = f.render(p.p_race_skills[0][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        for i in range(len(p.p_race_skills[0][2])):
            if p.p_race_skills[0][2][i] == "/":
                n.append(i)
        sk_func_1 = g.render(p.p_race_skills[0][2][:n[0]], 1, color)
        screen.blit(sk_func_1, (s.scr_x/2-145, 60))
        sk_func_2 = g.render(p.p_race_skills[0][2][n[0]:n[1]], 1, color)
        screen.blit(sk_func_2, (s.scr_x / 2 - 145, 80))
        sk_func_3 = g.render(p.p_race_skills[0][2][n[1]:], 1, color)
        screen.blit(sk_func_3, (s.scr_x / 2 - 145, 100))
        flag = False

    if pan == "skill_2_1":
        sk_name = f.render(p.p_spec_skills[0][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        sk_func = g.render(p.p_spec_skills[0][2], 1, color)
        screen.blit(sk_func, (s.scr_x/2-145, 60))
        flag = False
    if pan == "skill_2_2":
        sk_name = f.render(p.p_spec_skills[1][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        sk_func = g.render(p.p_spec_skills[1][2], 1, color)
        screen.blit(sk_func, (s.scr_x/2-145, 60))
        flag = False
    if pan == "skill_2_3":
        sk_name = f.render(p.p_spec_skills[2][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        sk_func = g.render(p.p_spec_skills[2][2], 1, color)
        screen.blit(sk_func, (s.scr_x/2-145, 60))
        flag = False
    if pan == "skill_2_4":
        sk_name = f.render(p.p_spec_skills[3][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        sk_func = g.render(p.p_spec_skills[3][2], 1, color)
        screen.blit(sk_func, (s.scr_x/2-145, 60))
        flag = False
    if pan == "skill_2_5":
        sk_name = f.render(p.p_spec_skills[4][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        sk_func = g.render(p.p_spec_skills[4][2], 1, color)
        screen.blit(sk_func, (s.scr_x/2-145, 60))
        flag = False
    if pan == "skill_2_6":
        sk_name = f.render(p.p_spec_skills[5][1], 1, color)
        screen.blit(sk_name, (s.scr_x/2-145, 25))
        sk_func = g.render(p.p_spec_skills[5][2], 1, color)
        screen.blit(sk_func, (s.scr_x/2-145, 60))
        flag = False
    if flag:
        s.co_back = True

    pygame.display.update()


# mana hp defence )))
def mahpde(screen, ra, sp):
    f = pygame.font.Font(None, 30)
    g = pygame.font.Font(None, 25)
    start = 240
    color = s.white
    n_hp = f.render(str(ra.hp + sp.hp) + "/" + str(ra.hp + sp.hp),
                    1, color)
    screen.blit(n_hp, (start, 70))
    n_mana = f.render(str(ra.mana + sp.mana) + "/" + str(ra.mana + sp.mana),
                      1, color)
    screen.blit(n_mana, (start-5, 140))
    n_def = f.render(str(ra.mana + sp.mana), 1, color)
    screen.blit(n_def, (start+5, 210))


# battle background
def battle_back(screen, ra, sp):
    global monster
    # f = pygame.font.Font(None, 28)
    # g = pygame.font.Font(None, 25)
    # color = s.white
    fon = pygame.image.load('pic/fon/forest_1.jpg')
    screen.blit(fon, (0, 0))
    back = pygame.image.load('pic/knipki/exit_01.jpg')
    screen.blit(back, (s.scr_x - 160, s.scr_y - 70))
    # hero
    screen.blit(p.player_big_pic, (40, 40))
    # monster
    screen.blit(monster, (s.scr_x - 220, 40))

    # stats player
    screen.blit(hp, (220, 50))
    screen.blit(mana, (220, 120))
    screen.blit(defen, (220, 190))
    # stats monster
    screen.blit(hp, (s.scr_x - 290, 50))
    screen.blit(mana, (s.scr_x - 290, 120))
    screen.blit(defen, (s.scr_x - 290, 190))

    # num
    mahpde(screen, ra, sp)
    # s.show_button(screen, 40, 40, 180, 320)
    # s.show_button(screen, s.scr_x - 220, 40, 180, 320)
#    for i in range(7):
#        s.show_button(screen, i*80+20, s.scr_y - 160, 60, 60)
#        s.show_button(screen, i*80+20, s.scr_y - 80, 60, 60)
#    screen.blit(p.p_race_skills[0], (20, s.scr_y - 160))

    pygame.display.update()


# battle skills show
def battle_skills(screen):
    race_skills = []
    spec_skills = []
    for i in range(len(p.p_race_skills)):
        race_skills.append(pygame.image.load(p.p_race_skills[i][0]))
        screen.blit(race_skills[i], (20, s.scr_y - 160))
    race_skills.clear()

    for i in range(len(p.p_spec_skills)):
        spec_skills.append(pygame.image.load(p.p_spec_skills[i][0]))
        screen.blit(spec_skills[i], (i*80 + 20, s.scr_y - 80))
    spec_skills.clear()

    pygame.display.update()


# start battle
def battle_check():
    # x = int(pg.a[pg.m - 5])
    y = int(pg.a[pg.m - 4])
    if pg.a[p.pos_y+y*3 + 3][p.pos_x] == '1':
        s.battle = True
