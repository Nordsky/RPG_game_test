import pygame
import setting as s
import time
import player as p
import gif_show as gs


# background
def blank_fon(screen):
    blank_surf = pygame.Surface((s.scr_x, s.scr_y))
    blank_surf.fill((0, 0, 0))
    screen.blit(blank_surf, (0, 0))
    time.sleep(0)



def title(screen):
    fon = pygame.image.load('pic/fon/title_1.jpg')
    screen.blit(fon, (0, 0))
    pygame.display.update()


def menu(screen):
    f = pygame.font.Font(None, 28)
    color = s.red
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    tut = pygame.image.load('pic/knipki/tutorial_01.jpg')
    screen.blit(tut, (s.scr_x / 2 - 150, 20))
    new = pygame.image.load('pic/knipki/newgame_01.jpg')
    screen.blit(new, (s.scr_x / 2 - 150, 140))
    back = pygame.image.load('pic/knipki/exit_01.jpg')
    screen.blit(back, (s.scr_x - 160, s.scr_y - 70))
    sett = pygame.image.load('pic/knipki/setting_01.jpg')
    screen.blit(sett, (30, 10))
    sk_name = f.render("Игра наиболее стабильна в разрешении 1000х550", 1, color)
    screen.blit(sk_name, (s.scr_x / 2 - 240, s.scr_y - 40))
    # s.show_button(screen, 30, 20, 150, 50)
    # s.show_button(screen, s.scrx/2-150, 20, 300, 60)      # tut
    # s.show_button(screen, s.scrx/2-150, 140, 300, 60)     # new game
    # s.show_button(screen, s.scrx-160, s.scry-70, 150, 60)   # back
    pygame.display.update()


def select_mode(screen):
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    easy = pygame.image.load('pic/fon/sloz_1.png')
    screen.blit(easy, (20, s.scr_y - 120))
    # s.show_button(screen, 20, s.scry-120, 180, 120)      #easy
    med = pygame.image.load('pic/fon/sloz_2.png')
    screen.blit(med, (s.scr_x / 2 - 90, s.scr_y - 120))
    # s.show_button(screen, s.scrx/2-90, s.scry-120, 180, 120)    #medium
    hard = pygame.image.load('pic/fon/sloz_3.png')
    screen.blit(hard, (s.scr_x - 200, s.scr_y - 120))
    # s.show_button(screen, s.scrx-200, s.scry-120, 180, 120)     #hard
    pygame.display.update()


def char_desk(screen):
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    # race
    human = pygame.image.load('pic/knipki/race_class/human_01.jpg')
    screen.blit(human, (10, 80))
    # s.show_button(screen, 10, 80, 100, 50)
    woodelf = pygame.image.load('pic/knipki/race_class/wood_elf_01.jpg')
    screen.blit(woodelf, (10, 150))
    # s.show_button(screen, 10, 150, 100, 50)

    orc = pygame.image.load('pic/knipki/race_class/orc_01.jpg')
    screen.blit(orc, (120, 80))
    dworf = pygame.image.load('pic/knipki/race_class/dwarf_01.jpg')
    screen.blit(dworf, (120, 150))
    # s.show_button(screen, 120, 80, 100, 50)

    # class
    warrior = pygame.image.load('pic/knipki/race_class/warrior_01.jpg')
    screen.blit(warrior, (s.scr_x - 220, 80))
    # s.show_button(screen, s.scrx-220, 80, 100, 50)
    archer = pygame.image.load('pic/knipki/race_class/arc_01.jpg')
    screen.blit(archer, (s.scr_x - 110, 80))
    # s.show_button(screen, s.scrx-220, 80, 100, 50)
    mage = pygame.image.load('pic/knipki/race_class/mage_01.jpg')
    screen.blit(mage, (s.scr_x - 220, 150))
    # s.show_button(screen, s.scrx-220, 150, 100, 50)

    # other
    # back = pygame.image.load('pic/knipki/exit_01.jpg')
    # screen.blit(back, (10, s.scr_y - 70))
    sled = pygame.image.load('pic/knipki/next_01.jpg')
    screen.blit(sled, (s.scr_x - 160, s.scr_y - 70))
    # s.show_button(screen, 10, s.scry-70, 150, 60)           # back
    # s.show_button(screen, s.scrx-160, s.scry-70, 150, 60)   # next
    # players_char = p.player_stand_pic
    # screen.blit(players_char, (s.scr_x/2-18, 5))
    # s.show_button(screen, s.scr_x/2-18, 5, 36, 36)           # back

    pygame.display.update()


def tutorial(screen):
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    back = pygame.image.load('pic/knipki/exit_01.jpg')
    screen.blit(back, (s.scr_x - 160, s.scr_y - 70))
    # s.show_button(screen, s.scrx-160, s.scry-70, 150, 60)   # back
    pygame.display.update()


# chat screen )
def chat_screen(screen):
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    back = pygame.image.load('pic/knipki/exit_01.jpg')
    screen.blit(back, (s.scr_x - 160, s.scr_y - 70))
    # s.show_button(screen, s.scrx-160, s.scry-70, 150, 60)   # back
    pygame.display.update()


# show skills sum
def show_sum(screen, race, spec, pos):
    f = pygame.font.Font(None, 30)
    start = 0
    if pos == 1:
        start = s.scr_x / 2 - 20
    if pos == 2:
        start = s.scr_x - 100
    if pos == 3:
        start = s.scr_x -50
    color = s.cyan
    hp = f.render(str(race.hp+spec.hp), 1, color)
    df = f.render(str(race.df+spec.df), 1, color)
    mana = f.render(str(race.mana+spec.mana), 1, color)
    st = f.render(str(race.st+spec.st), 1, color)
    re = f.render(str(race.re+spec.re), 1, color)
    vo = f.render(str(race.vo+spec.vo), 1, color)
    har = f.render(str(race.har+spec.har), 1, color)
    speed = f.render(str(race.speed+spec.speed), 1, color)
    #vnim = f.render(str(race.vnim+spec.vnim), 1, color)
    #sluh = f.render(str(race.sluh+spec.sluh), 1, color)
    #shadow = f.render(str(race.shadow+spec.shadow), 1, color)
    #noise = f.render(str(race.noise+spec.noise), 1, color)
    gold = f.render(str(race.gold+spec.gold), 1, color)

    screen.blit(hp, (start, s.top_start+1*s.step_y))
    screen.blit(df, (start, s.top_start+2*s.step_y))
    screen.blit(mana, (start, s.top_start+3*s.step_y))
    screen.blit(st, (start, s.top_start+4*s.step_y))
    screen.blit(re, (start, s.top_start+5*s.step_y))
    screen.blit(vo, (start, s.top_start+6*s.step_y))
    screen.blit(har, (start, s.top_start+7*s.step_y))
    screen.blit(speed, (start, s.top_start+8*s.step_y))
    #screen.blit(vnim, (start, s.top_start+9*s.step_y))
    #screen.blit(sluh, (start, s.top_start+10*s.step_y))
    #screen.blit(shadow, (start, s.top_start+11*s.step_y))
    #screen.blit(noise, (start, s.top_start+12*s.step_y))
    screen.blit(gold, (start, s.top_start+9*s.step_y))


# setting
def setting_menu(screen):
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    back = pygame.image.load('pic/knipki/exit_01.jpg')
    screen.blit(back, (s.scr_x - 160, s.scr_y - 70))
    f1 = pygame.image.load('pic/knipki/sc_1280_1024.jpg')
    screen.blit(f1, (20, 20))
    # s.show_button(screen, 20, 20, 130, 40)
    f2 = pygame.image.load('pic/knipki/sc_1366_768.jpg')
    screen.blit(f2, (20, 70))
    # s.show_button(screen, 20, 70, 130, 40)
    f3 = pygame.image.load('pic/knipki/sc_1920_1080.jpg')
    screen.blit(f3, (20, 120))
    # s.show_button(screen, 20, 120, 130, 40)
    f4 = pygame.image.load('pic/knipki/sc_1024_768.jpg')
    screen.blit(f4, (20, 170))
    # s.show_button(screen, 20, 170, 130, 40)
    f5 = pygame.image.load('pic/knipki/sc_900_600.jpg')
    screen.blit(f5, (20, 220))
    # s.show_button(screen, 20, 220, 130, 40)
    f6 = pygame.image.load('pic/knipki/sc_1440_900.jpg')
    screen.blit(f6, (20, 270))
    f = pygame.font.Font(None, 25)
    color = s.cyan
    vol_param = int(s.so_vol*10//1)
    if vol_param > 10:
        vol_param -= 1
        s.so_vol -= 1.1
    if vol_param < 0:
        vol_param += 1
        s.so_vol += 1.1
    vol_text = str(vol_param*10) + " %"
    vol = f.render(vol_text, 1, color)
    screen.blit(vol, (s.scr_x - 80, 80))
    minus = pygame.image.load('pic/knipki/vol_min_01.jpg')
    screen.blit(minus, (s.scr_x - 120, 20))
    plus = pygame.image.load('pic/knipki/vol_plus_01.jpg')
    screen.blit(plus, (s.scr_x - 60, 20))
    # s.show_button(screen, s.scr_x - 120, 20, 40, 40)
    # s.show_button(screen, s.scr_x - 60, 20, 40, 40)
    # s.show_button(screen, s.scrx-160, s.scry-70, 150, 60)   # back
    pygame.display.update()


# no comment
def show_stats_text(screen, pos):
    f = pygame.font.Font(None, 25)
    start = pos
    color = s.cyan
    hp = f.render("Здоровье:", 1, color)
    df = f.render("Защита:", 1, color)
    mana = f.render("Мана:", 1, color)
    st = f.render("Стойкость:", 1, color)
    re = f.render("Реакция:", 1,  color)
    vo = f.render("Воля:", 1, color)
    har = f.render("Харизма:", 1, color)
    speed = f.render("Скорость:", 1, color)
    #vnim = f.render("Зрение:", 1, color)
    #sluh = f.render("Слух:", 1, color)
    #shadow = f.render("Скрытность:", 1, color)
    #noise = f.render("Шум:", 1, color)
    gold = f.render("Золото:", 1, color)

    screen.blit(hp, (start, s.top_start+1*s.step_y))
    screen.blit(df, (start, s.top_start+2*s.step_y))
    screen.blit(mana, (start, s.top_start+3*s.step_y))
    screen.blit(st, (start, s.top_start+4*s.step_y))
    screen.blit(re, (start, s.top_start+5*s.step_y))
    screen.blit(vo, (start, s.top_start+6*s.step_y))
    screen.blit(har, (start, s.top_start+7*s.step_y))
    screen.blit(speed, (start, s.top_start+8*s.step_y))
    #screen.blit(vnim, (start, s.top_start+9*s.step_y))
    #screen.blit(sluh, (start, s.top_start+10*s.step_y))
    #screen.blit(shadow, (start, s.top_start+11*s.step_y))
    #screen.blit(noise, (start, s.top_start+12*s.step_y))
    screen.blit(gold, (start, s.top_start+9*s.step_y))


# AAA
def show_stats(screen, race, pos):
    f = pygame.font.Font(None, 30)
    start = pos
    color = s.cyan
    name = f.render(str(race.name), 1, color)
    hp = f.render(str(race.hp), 1, color)
    df = f.render(str(race.df), 1, color)
    mana = f.render(str(race.mana), 1, color)
    st = f.render(str(race.st), 1, color)
    re = f.render(str(race.re), 1, color)
    vo = f.render(str(race.vo), 1, color)
    har = f.render(str(race.har), 1, color)
    speed = f.render(str(race.speed), 1, color)
    #vnim = f.render(str(race.vnim), 1, color)
    #sluh = f.render(str(race.sluh), 1, color)
    #shadow = f.render(str(race.shadow), 1, color)
    #noise = f.render(str(race.noise), 1, color)
    gold = f.render(str(race.gold), 1, color)

    screen.blit(name, (start, s.top_start))
    screen.blit(hp, (start + s.step_x, s.top_start + 1 * s.step_y))
    screen.blit(df, (start + s.step_x, s.top_start + 2 * s.step_y))
    screen.blit(mana, (start + s.step_x, s.top_start + 3 * s.step_y))
    screen.blit(st, (start + s.step_x, s.top_start + 4 * s.step_y))
    screen.blit(re, (start + s.step_x, s.top_start + 5 * s.step_y))
    screen.blit(vo, (start + s.step_x, s.top_start + 6 * s.step_y))
    screen.blit(har, (start + s.step_x, s.top_start + 7 * s.step_y))
    screen.blit(speed, (start + s.step_x, s.top_start + 8 * s.step_y))
    #screen.blit(vnim, (start + s.step_x, s.top_start + 9 * s.step_y))
    #screen.blit(sluh, (start + s.step_x, s.top_start + 10 * s.step_y))
    #screen.blit(shadow, (start + s.step_x, s.top_start + 11 * s.step_y))
    #screen.blit(noise, (start + s.step_x, s.top_start + 12 * s.step_y))
    screen.blit(gold, (start + s.step_x, s.top_start + 9 * s.step_y))


# WTF is it ?!
def pole(screen):
    surf = pygame.Surface((s.mainx, s.mainy))
    surf.fill((255, 255, 255))
    warr = pygame.image.load('pic/icon/warrior_01.jpg')
    for i in range(2, s.pscalex+2):
        for j in range(2, s.pscaley+2):
            screen.blit(warr, (i*s.sot, j*s.sot))
    # screen.blit(surf, (70, 50))
    pygame.display.update()


# delete this !!!!!!!!!!!!
def left_pan(screen):
    surf = pygame.Surface((70, s.mainy))
    surf.fill((230, 230, 230))
    screen.blit(surf, (0, 50))
    pygame.display.update()


def right_pan(screen):
    surf = pygame.Surface((s.scr_x - s.mainx - 70, s.scr_y))
    surf.fill((200, 200, 200))
    screen.blit(surf, (s.mainx+70, 0))
    pygame.display.update()


def top_pan(screen):
    surf = pygame.Surface((s.mainx+70, 50))
    surf.fill((170, 170, 170))
    screen.blit(surf, (0, 0))
    pygame.display.update()
