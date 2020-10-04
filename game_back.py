import pygame
import player as p
import setting as s
import pole_gener as pg
import chat_setting as cs
import random as r


"""def tteesstt(screen, race, spec, pos):
    f = pygame.font.Font(None, 30)
    start = 0
    if pos == 1:
        start = s.scr_x / 2 - 20
    if pos == 2:
        start = s.scr_x - 100
    color = s.cyan
    hp = f.render(str(race.hp+spec.hp), 1, color)
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    tut = pygame.image.load('pic/knipki/tutorial_01.jpg')
    screen.blit(tut, (s.scr_x / 2 - 150, 20))
    new = pygame.image.load('pic/knipki/newgame_01.jpg')
    screen.blit(new, (s.scr_x / 2 - 150, 140))
    back = pygame.image.load('pic/knipki/exit_01.jpg')
    screen.blit(back, (s.scr_x - 160, s.scr_y - 70))
    s.show_button(screen, 30, 20, 150, 50)
    # s.show_button(screen, s.scrx/2-150, 20, 300, 60)      # tut
    # s.show_button(screen, s.scrx/2-150, 140, 300, 60)     # new game
    # s.show_button(screen, s.scrx-160, s.scry-70, 150, 60)   # back
    pygame.display.update()
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
    screen.blit(vol, (80, s.scx-80))

    """

race = p.player_race(p.player_lvl)
spec = p.player_spec(p.player_lvl)
x = int(pg.a[pg.m - 5])
y = int(pg.a[pg.m - 4])
posx = p.pos_x
posy = p.pos_y


def chat_all_events(screen):
    fon = pygame.image.load('pic/fon/stand_01.jpg')
    screen.blit(fon, (0, 0))
    cs.chat_print(cs.chat, screen)


def chat_event(screen, nx, ny, y, race):
    if pg.a[ny+y*2 + 2][nx] == '1':
        g = r.randint(1, 5)
        race.gold += g
        cs.chat_check(screen, p.pos_x, p.pos_y, pg.y, cs.chat, g)
        pg.a[ny+y*2 + 2] = pg.a[ny+y*2 + 2][:nx] + "b" + pg.a[ny+y*2 + 2][nx+1:]
        s.co_text = True
        s.co_chat = True
    else:
        cs.chat_check(screen, p.pos_x, p.pos_y, pg.y, cs.chat, 0)
        s.co_text = True
        s.co_chat = True


def chat_pan(screen):
    cs.chat_print(cs.chat, screen)
    cs.chat_all_print(cs.chat, screen)
    pygame.display.update()


def left_pan(screen):
    surf = pygame.Surface((s.scr_x/2, 100))
    surf.fill((20, 20, 20))
    screen.blit(surf, (0, s.scr_y-100))
    cs.chat_print(cs.chat, screen)
    sett = pygame.image.load('pic/knipki/chat_all_01.jpg')
    screen.blit(sett, (s.scr_x/2 - 20, s.scr_y - 100))
    # s.show_button(screen, s.scr_x/2 - 20, s.scr_y - 100, 20, 50)
    pygame.display.update()


def right_pan(screen):
    surf = pygame.Surface((s.scr_x / 2, 100))
    surf.fill((50, 50, 50))
    screen.blit(surf, (s.scr_x/2, s.scr_y - 100))
    sett = pygame.image.load('pic/knipki/setting_small_01.jpg')
    screen.blit(sett, (s.scr_x - 50, s.scr_y - 100))
    game_exit = pygame.image.load('pic/knipki/exit_small_01.jpg')
    screen.blit(game_exit, (s.scr_x - 50, s.scr_y - 50))
    # s.show_button(screen, s.scr_x - 50, s.scr_y - 50, 50, 50)   # back
    # s.show_button(screen, s.scr_x - 50, s.scr_y - 100, 50, 50)
    pygame.display.update()


def stat_pan(screen):
    surf = pygame.Surface((300, s.scr_y-100))
    surf.fill((70, 70, 70))
    screen.blit(surf, (s.scr_x-300, 0))
    f = pygame.font.Font(None, 30)
    color = s.cyan
    loc_name = f.render(pg.a[pg.m-3][0:len(pg.a[pg.m-3])-1], 1, color)
    screen.blit(loc_name, (s.scr_x-280, 10))
    f = pygame.font.Font(None, 24)
    loc_lvl = f.render("Уровень локации : " + pg.a[pg.m-2][0:len(pg.a[pg.m-2])-1], 1, color)
    screen.blit(loc_lvl, (s.scr_x-280, 30))
    pygame.display.update()


def test_pan(screen):
    surf = pygame.Surface((s.sot*22, s.sot*14))
    surf.fill((100, 100, 100))
    screen.blit(surf, (0, 0))
    pygame.display.update()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_event_key():
    print("test key move")