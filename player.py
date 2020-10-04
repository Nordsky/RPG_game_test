import pygame
import race as r
import spec as s
import spells as z

player_lvl = 1
player_race = r.Human
player_spec = s.Warrior
player_move = 1
player_sost = 3
pgold = 0
# start_pos_x = 5
# start_pos_y = 5
pos_x = 5
pos_y = 3
player_mode = 1

player_quest = {}
player_compl_quest = []
player_set = {}
player_invent = []
p_race_skills = []
p_spec_skills = []
player_perk = []
player_gold = 0

player_pos = []
key = 1

enemy_hello = 0
enemy_bye = 0
deaths = 0

player_stand_pic = pygame.image.load('pic/icon/player_1.png')

player_big_pic = pygame.image.load('pic/icon/hum_war.jpg')

p_race_skills.append(z.human_1)


def check_player_skill(race, spec):
    global p_race_skills
    global p_spec_skills
    if race == "Человек":
        p_race_skills.clear()
        p_race_skills.append(z.human_1)
    if race == "Лесной эльф":
        p_race_skills.clear()
        p_race_skills.append(z.elf_1)
    if race == "Орк":
        p_race_skills.clear()
        p_race_skills.append(z.orc_1)
    if race == "Дворф":
        p_race_skills.clear()
        p_race_skills.append(z.dworf_1)

    if spec == "Воин":
        p_spec_skills.clear()
        p_spec_skills.append(z.war_1)
        p_spec_skills.append(z.war_2)
        p_spec_skills.append(z.war_3)
        p_spec_skills.append(z.war_4)
        p_spec_skills.append(z.war_5)
        p_spec_skills.append(z.war_6)
    if spec == "Волшебник":
        p_spec_skills.clear()
        p_spec_skills.append(z.mag_1)
        p_spec_skills.append(z.mag_2)
        p_spec_skills.append(z.mag_3)
        p_spec_skills.append(z.mag_4)
        p_spec_skills.append(z.mag_5)
        p_spec_skills.append(z.mag_6)
    if spec == "Лучник":
        p_spec_skills.clear()
        p_spec_skills.append(z.arc_1)
        p_spec_skills.append(z.arc_2)
        p_spec_skills.append(z.arc_3)
        p_spec_skills.append(z.arc_4)
        p_spec_skills.append(z.arc_5)
        p_spec_skills.append(z.arc_6)


def check_player_ico(race, spec):
    global player_stand_pic
    global player_big_pic
    if race == "Человек" and spec == "Воин":
        player_big_pic = pygame.image.load('pic/icon/hum_war.jpg')
    if race == "Человек" and spec == "Волшебник":
        player_big_pic = pygame.image.load('pic/icon/hum_mage.jpg')
    if race == "Человек" and spec == "Лучник":
        player_big_pic = pygame.image.load('pic/icon/hum_arc.jpg')

    if race == "Лесной эльф" and spec == "Воин":
        player_big_pic = pygame.image.load('pic/icon/elf_war.jpg')
    if race == "Лесной эльф" and spec == "Волшебник":
        player_big_pic = pygame.image.load('pic/icon/elf_mage.jpg')
    if race == "Лесной эльф" and spec == "Лучник":
        player_big_pic = pygame.image.load('pic/icon/elf_arc.jpg')

    if race == "Орк" and spec == "Воин":
        player_big_pic = pygame.image.load('pic/icon/orc_war.jpg')
    if race == "Орк" and spec == "Волшебник":
        player_big_pic = pygame.image.load('pic/icon/orc_mage.jpg')
    if race == "Орк" and spec == "Лучник":
        player_big_pic = pygame.image.load('pic/icon/orc_arc.jpg')

    if race == "Дворф" and spec == "Воин":
        player_big_pic = pygame.image.load('pic/icon/dworf_war.jpg')
    if race == "Дворф" and spec == "Волшебник":
        player_big_pic = pygame.image.load('pic/icon/dworf_mage.jpg')
    if race == "Дворф" and spec == "Лучник":
        player_big_pic = pygame.image.load('pic/icon/dworf_arc.jpg')


def no_trans(x, y, max_x, max_y):
    global pos_x
    global pos_y
    if x > max_x-1:
        pos_x -= 1
    if x < 0:
        pos_x += 1
    if y > max_y-1:
        pos_y -= 1
    if y < 0:
        pos_y += 1


def player_trans(max_x, max_y):
    global player_pos
    global pos_x
    global pos_y
    global key
    if key == 1:
        for i in range(max_y):
            for j in range(max_x):
                player_pos[i][j] = '0'
        for i in range(max_y):
            for j in range(max_x):
                no_trans(pos_x, pos_y, max_x, max_y)
                if i == pos_y and j == pos_x:
                    player_pos[i][j] = '1'


def player_plane(x, y):
    global player_pos
    for i in range(y):
        player_pos.append([])
        for j in range(x):
            if i == pos_y and j == pos_x:
                player_pos[i].append('1')
            else:
                player_pos[i].append('0')


class Player():
    def __init__(self, lvl, name, race, spec):
        self.lvl = lvl
        self.name = name
        self.race = race
        self.spec = spec
        self.gold = 0
