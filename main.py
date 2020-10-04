import pygame
import setting as s
import func_back as fb
import race as r
import player as p
import spec as sp
import pole_gener as pg
import game_back as gb
import sound_sets as ss
import chat_setting as cs
import battle as ba
import gif_show as gs

pygame.init()
screen = pygame.display.set_mode((s.scr_x, s.scr_y))
pygame.display.set_caption("Lost Tales Adventure   v 0.8")


def chat_all_screen():
    fb.chat_screen(screen)
    gb.chat_pan(screen)
    while s.chat_all:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.chat_all = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.ca_id)
                    if click == "exit":
                        s.chat_all = False
                        s.co_back = True
                        s.co_text = True

    if s.co_text:
        gb.chat_pan(screen)


def tut_screen():
    fb.tutorial(screen)
    while s.tut:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.tut = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.t_id)
                    if click == "exit":
                        s.tut = False
                        s.co_back = True
        # fb.tutorial(screen)
        # pygame.display.flip()
        # s.clock.tick(s.fps)


fb.blank_fon(screen)


def battle_plane():
    pan = 0
    race = p.player_race(p.player_lvl)
    spec = p.player_spec(p.player_lvl)
    ba.battle_back(screen, race, spec)
    ba.battle_skills(screen)
    # ba.random_enemy()
    sk_show = False
    while s.battle:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.battle = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.b_id)
                    if click == "exit":
                        s.battle = False
                        s.co_back = True
                        s.co_text = True
                if e.button == s.right_m:
                    pan = s.check_mouse(e.pos[0], e.pos[1], s.b_id)
                    sk_show = True
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == s.right_m:
                    sk_show = False
                    s.co_back = True
        if sk_show:
            ba.spell_info(screen, pan)            

        if s.co_back:
            race = p.player_race(p.player_lvl)
            spec = p.player_spec(p.player_lvl)
            ba.battle_back(screen, race, spec)
            ba.battle_skills(screen)
            pygame.display.flip()
            s.co_back = False
        

def setting_screen():
    fb.setting_menu(screen)
    while s.sett:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.sett = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.s_id)
                    if click == "exit":
                        s.sett = False
                        s.co_back = True
                        s.co_text = True
                    if click == "so_vol_plus":
                        s.so_vol += 0.11
                        s.co_back = True
                    if click == "so_vol_minus":
                        s.so_vol -= 0.11
                        s.co_back = True
                    if click == "size_1":
                        s.scr_x = 1280
                        s.scr_y = 1024
                        s.r_start = s.scr_x - 380
                        pygame.display.set_mode((s.scr_x, s.scr_y))
                        s.co_back = True
                    if click == "size_2":
                        s.scr_x = 1366
                        s.scr_y = 768
                        s.r_start = s.scr_x - 380
                        pygame.display.set_mode((s.scr_x, s.scr_y))
                        s.co_back = True
                    if click == "size_3":
                        s.scr_x = 1920
                        s.scr_y = 1080
                        s.r_start = s.scr_x - 380
                        pygame.display.set_mode((s.scr_x, s.scr_y))
                        s.co_back = True
                    if click == "size_4":
                        s.scr_x = 1024
                        s.scr_y = 768
                        s.r_start = s.scr_x - 380
                        pygame.display.set_mode((s.scr_x, s.scr_y))
                        s.co_back = True
                    if click == "size_5":
                        s.scr_x = 1000
                        s.scr_y = 600
                        s.r_start = s.scr_x - 380
                        pygame.display.set_mode((s.scr_x, s.scr_y))
                        s.co_back = True
                    if click == "size_6":
                        s.scr_x = 1440
                        s.scr_y = 900
                        s.r_start = s.scr_x - 380
                        pygame.display.set_mode((s.scr_x, s.scr_y))
                        s.co_back = True
    
        if s.co_back:
            fb.setting_menu(screen)
            pygame.display.flip()
            s.co_back = False
        # s.clock.tick(s.fps)


fb.blank_fon(screen)


def check_mode():
    fb.select_mode(screen)
    while s.mode:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.mode = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.m_id)
                    if click == "easy":
                        p.player_mode = 1
                        s.mode = False
                        s.create_char = True
                        s.main_menu = False
                    if click == "medium":
                        p.player_mode = 2
                        s.mode = False
                        s.create_char = True
                        s.main_menu = False
                    if click == "hard":
                        p.player_mode = 3
                        s.mode = False
                        s.create_char = True
                        s.main_menu = False
                    if click == "exit":
                        s.mode = False
        # fb.select_mode(screen)
        # pygame.display.flip()
        # s.clock.tick(s.fps)


fb.blank_fon(screen)


def title_screen():
    k = 0
    clock = pygame.time.Clock()
    FPS = 30
    gs.gif_check()
    fb.title(screen)
    while s.tit_scr:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.tit_scr = False
                exit()
            if e.type == pygame.KEYDOWN:
                s.tit_scr = False
                s.main_menu = True
    
        k += 1
        if k >= 6:
            k = 0
        fb.title(screen)
        screen.blit(gs.z[k], (s.scr_x/2 - 380, 130))
        screen.blit(gs.z[k], (s.scr_x/2 + 50, 130))
        pygame.display.update()
        clock.tick(6)


title_screen()
fb.blank_fon(screen)


def menu():
    fb.menu(screen)
    while s.main_menu:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.main_menu = False
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.mm_id)
                    if click == "new":
                        s.mode = True
                        fb.blank_fon(screen)
                        check_mode()
                    if click == "tutorial":
                        s.tut = True
                        fb.blank_fon(screen)
                        tut_screen()
                        s.co_back = True
                    if click == "setting":
                        s.sett = True
                        fb.blank_fon(screen)
                        setting_screen()
                        s.co_back = True
                    if click == "exit":
                        s.main_menu = False
                        exit()

        if s.co_back:
            fb.menu(screen)
            s.co_back = False
        # pygame.display.flip()
        # s.clock.tick(s.fps)


menu()
fb.blank_fon(screen)


def create_character():
    check_race = r.Human(p.player_lvl)
    check_spec = sp.Warrior(p.player_lvl)
    fb.char_desk(screen)
    screen.blit(p.player_big_pic, (s.scr_x / 2 - 80, 10))
    # fb.show_sum(screen, check_race, check_spec, 1)
    fb.show_stats_text(screen, s.l_start)
    fb.show_stats(screen, check_race, s.l_start)
    fb.show_stats_text(screen, s.r_start)
    fb.show_stats(screen, check_spec, s.r_start)
    p.check_player_ico(check_race.name, check_spec.name)
    p.check_player_skill(check_race.name, check_spec.name)
    ba.battle_skills(screen)
    pygame.display.update()
    while s.create_char:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.create_char = False
                exit()
                # s.game = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.cc_id)
                    if click == "Human":
                        check_race = r.Human(p.player_lvl)
                        p.player_race = r.Human
                        s.co_text = True
                    if click == "Wood elf":
                        check_race = r.WoodElf(p.player_lvl)
                        p.player_race = r.WoodElf
                        s.co_text = True

                    if click == "Orc":
                        p.player_race = "Orc"
                        check_race = r.Orc(p.player_lvl)
                        p.player_race = r.Orc
                        s.co_text = True
                    if click == "Dworf":
                        p.player_race = "Dworf"
                        check_race = r.Dworf(p.player_lvl)
                        p.player_race = r.Dworf
                        s.co_text = True

                    if click == "Warrior":
                        p.player_spec = sp.Warrior
                        check_spec = sp.Warrior(p.player_lvl)
                        s.co_text = True
                    if click == "Wizard":
                        p.player_spec = sp.Wizard
                        check_spec = sp.Wizard(p.player_lvl)
                        s.co_text = True

                    if click == "Archer":
                        p.player_spec = sp.Archer
                        check_spec = sp.Archer(p.player_lvl)
                        s.co_text = True

                    if click == "next":
                        s.create_char = False
                        s.game = True
                    # if click == "exit":
                        # s.create_char = False
                        # exit()

        if s.co_text:
            p.check_player_ico(check_race.name, check_spec.name)
            p.check_player_skill(check_race.name, check_spec.name)
            fb.char_desk(screen)
            screen.blit(p.player_big_pic, (s.scr_x/2-80, 10))
            # fb.show_sum(screen, check_race, check_spec, 1)
            fb.show_stats_text(screen, s.l_start)
            fb.show_stats(screen, check_race, s.l_start)
            fb.show_stats_text(screen, s.r_start)
            fb.show_stats(screen, check_spec, s.r_start)
            ba.battle_skills(screen)
            pygame.display.flip()
            s.co_text = False
        # p.player_gold = check_race.gold + check_spec.gold
        # p.check_player_ico(check_spec.name)

        # pygame.display.update()
        # s.clock.tick(s.fps)


create_character()
player = p.Player(p.player_lvl,
                  "name",
                  p.player_race,
                  p.player_spec)
fb.blank_fon(screen)


def run_game():
    s.co_back = True
    s.co_text = True
    s.co_moved = True
    race = p.player_race(p.player_lvl)
    spec = p.player_spec(p.player_lvl)
    pg.check_loc('0003')
    cs.chat_gener(cs.chat)
    x = int(pg.a[pg.m - 5])
    y = int(pg.a[pg.m - 4])
    p.player_plane(30, 30)
    gb.left_pan(screen)
    gb.right_pan(screen)
    gb.stat_pan(screen)
    pg.paint_back(screen)
    pg.paint_door(screen)
    pg.paint_decor(screen)
    pg.paint_monster(screen)
    pg.paint_player(screen)
    # pg.sun_moon(1, p.pos_x, p.pos_y)
    # pg.paint_night(screen)
    fb.show_sum(screen, race, spec, 2)
    while s.game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                s.game = False
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == s.left_m:
                    click = s.check_click(e.pos[0], e.pos[1], s.g_id)
                    if click == "setting":
                        s.sett = True
                        fb.blank_fon(screen)
                        setting_screen()
                        screen.blit(pg.surf, (0, 0))
                        s.co_back = True
                        s.co_moved = True
                    if click == "allchat":
                        s.chat_all = True
                        fb.blank_fon(screen)
                        chat_all_screen()
                        screen.blit(pg.surf, (0, 0))
                        s.co_back = True
                        s.co_moved = True
                        s.co_text = True
                    if click == "exit":
                        s.game = False
                        exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    ss.check_sound(1, pg.a[p.pos_y][p.pos_x])
                    p.pos_y -= 1
                    p.no_trans(p.pos_x, p.pos_y, x, y)
                    pg.trans_loc(screen, p.pos_x, p.pos_y + y + 1)
                    pg.no_move(p.pos_x, p.pos_y, 1)
                    gb.chat_event(screen, p.pos_x, p.pos_y, y, race)
                    p.player_trans(x, y)
                    ba.battle_check()
                    if s.battle:
                        ba.random_enemy()
                        battle_plane()
                        screen.blit(pg.surf, (0, 0))
                    s.co_moved = True
                if e.key == pygame.K_s:
                    ss.check_sound(1, pg.a[p.pos_y][p.pos_x])
                    p.pos_y += 1
                    p.no_trans(p.pos_x, p.pos_y, x, y)
                    pg.trans_loc(screen, p.pos_x, p.pos_y + y + 1)
                    pg.no_move(p.pos_x, p.pos_y, 2)
                    gb.chat_event(screen, p.pos_x, p.pos_y, y, race)
                    p.player_trans(x, y)
                    ba.battle_check()
                    if s.battle:
                        ba.random_enemy()
                        battle_plane()
                        screen.blit(pg.surf, (0, 0))
                    s.co_moved = True
                if e.key == pygame.K_a:
                    ss.check_sound(1, pg.a[p.pos_y][p.pos_x])
                    p.pos_x -= 1
                    p.no_trans(p.pos_x, p.pos_y, x, y)
                    pg.trans_loc(screen, p.pos_x, p.pos_y + y + 1)
                    pg.no_move(p.pos_x, p.pos_y, 3)
                    gb.chat_event(screen, p.pos_x, p.pos_y, y, race)
                    p.player_trans(x, y)
                    ba.battle_check()
                    if s.battle:
                        ba.random_enemy()
                        battle_plane()
                        screen.blit(pg.surf, (0, 0))
                    s.co_moved = True
                if e.key == pygame.K_d:
                    ss.check_sound(1, pg.a[p.pos_y][p.pos_x])
                    p.pos_x += 1
                    p.no_trans(p.pos_x, p.pos_y, x, y)
                    pg.trans_loc(screen, p.pos_x, p.pos_y + y + 1)
                    pg.no_move(p.pos_x, p.pos_y, 4)
                    gb.chat_event(screen, p.pos_x, p.pos_y, y, race)
                    p.player_trans(x, y)
                    ba.battle_check()
                    if s.battle:
                        ba.random_enemy()
                        battle_plane()
                        screen.blit(pg.surf, (0, 0))
                    s.co_moved = True

        if s.co_back:
            gb.left_pan(screen)
            gb.right_pan(screen)
            gb.stat_pan(screen)
            # gb.test_pan(screen)
            pygame.display.update()
            s.co_back = False

        if s.co_moved:
            pg.paint_back(screen)
            pg.paint_door(screen)
            pg.paint_decor(screen)
            pg.paint_monster(screen)
            pygame.display.update()
            pg.paint_player(screen)
            pg.sun_moon(pg.check_light(), p.pos_x, p.pos_y)
            pg.paint_night(screen)
            pygame.display.update()
            s.co_moved = False

        if s.co_text:
            gb.left_pan(screen)
            gb.right_pan(screen)
            gb.stat_pan(screen)
            fb.show_sum(screen, race, spec, 3)
            pygame.display.update()
            s.co_text = False

        if s.co_chat:
            gb.left_pan(screen)
            s.co_chat = False

        x = int(pg.a[pg.m - 5])
        y = int(pg.a[pg.m - 4])
        # pygame.display.flip()
        s.clock.tick(s.fps)


run_game()
