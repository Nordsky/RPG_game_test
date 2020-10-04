import pygame

sot = 36  # 36
# screen scale
scr_x = 1000  # 1100
scr_y = 550  # 600

# pole scale
pscalex = 18
pscaley = 12

mainx = sot*pscalex
mainy = sot*pscaley

# window
main_menu = True
mm_id = 1
create_char = False
cc_id = 2
tut = False
t_id = 3
mode = False
m_id = 4
sett = False
s_id = 5
battle = False
b_id = 6
chat_all = False
ca_id = 7
tit_scr = True
ti_id = 8
game = False
g_id = 9

# colors
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 200, 100)
black = (0, 0, 0)
white = (255, 255, 255)

# character gener const
step_x = 110
step_y = 30
l_start = 250
r_start = scr_x - 380
top_start = 20
# game const
co_back = False
co_text = False
co_moved = False
co_chat = False
co_tik = True

chat_start = True

# other
so_vol = 0.0
mu_vol = 0.0
fps = 30
clock = pygame.time.Clock()
left_m = 1
right_m = 3

# button functions


def show_button(screen, xs, ys, x, y):
    pygame.draw.rect(screen, (100, 0, 100), (xs, ys, x, y))


def check_mouse(x, y, loc_id):
    if loc_id == 6:
        # up
        if 80 > x > 20 \
                and scr_y - 100 > y > scr_y - 160:
            return "skill_1_1"
        # down
        if 80 > x > 20 \
                and scr_y - 20 > y > scr_y - 80:
            return "skill_2_1"
        if 160 > x > 100 \
                and scr_y - 20 > y > scr_y - 80:
            return "skill_2_2"
        if 240 > x > 180 \
                and scr_y - 20 > y > scr_y - 80:
            return "skill_2_3"
        if 300 > x > 260 \
                and scr_y - 20 > y > scr_y - 80:
            return "skill_2_4"
        if 380 > x > 320 \
                and scr_y - 20 > y > scr_y - 80:
            return "skill_2_5"
        if 460 > x > 400 \
                and scr_y - 20 > y > scr_y - 80:
            return "skill_2_6"


def check_click(x, y, loc_id):
    # menu
    if loc_id == 1:
        if scr_x/2+150 > x > scr_x/2-150 \
                and 200 > y > 140:
            return "new"
        if scr_x/2+150 > x > scr_x/2-150 \
                and 80 > y > 20:
            return "tutorial"
        if scr_x-10 > x > scr_x-160 \
                and scr_y-10 > y > scr_y-70:
            return "exit"
        if 180 > x > 30 \
                and 70 > y > 20:
            return "setting"

    # tutorial
    if loc_id == 3:
        if scr_x-10 > x > scr_x-160 \
                and scr_y-10 > y > scr_y-70:
            return "exit"

    # chat all
    if loc_id == 7:
        if scr_x-10 > x > scr_x-160 \
                and scr_y-10 > y > scr_y-70:
            return "exit"

    # chat all
    if loc_id == 6:
        if scr_x-10 > x > scr_x-160 \
                and scr_y-10 > y > scr_y-70:
            return "exit"    

    # setting
    if loc_id == 5:
        if scr_x-10 > x > scr_x-160 \
                and scr_y-10 > y > scr_y-70:
            return "exit"
        if scr_x-80 > x > scr_x-120 \
                and 60 > y > 20:
            return "so_vol_minus"
        if scr_x-20 > x > scr_x-60 \
                and 60 > y > 20:
            return "so_vol_plus"
        if 150 > x > 20 \
                and 60 > y > 20:
            return "size_1"
        if 150 > x > 20 \
                and 110 > y > 70:
            return "size_2"
        if 150 > x > 20 \
                and 160 > y > 120:
            return "size_3"
        if 150 > x > 20 \
                and 210 > y > 170:
            return "size_4"
        if 150 > x > 20 \
                and 260 > y > 220:
            return "size_5"
        if 150 > x > 20 \
                and 310 > y > 270:
            return "size_6"

    # create character
    if loc_id == 2:
        # race
        if 110 > x > 10 \
                and 130 > y > 80:
            return "Human"
        if 110 > x > 10 \
                and 200 > y > 150:
            return "Wood elf"

        if 220 > x > 120 \
                and 130 > y > 80:
            return "Orc"
        if 220 > x > 120 \
                and 200 > y > 150:
            return "Dworf"

        # class
        if scr_x-120 > x > scr_x-220 \
                and 130 > y > 80:
            return "Warrior"
        if scr_x-120 > x > scr_x-220 \
                and 200 > y > 150:
            return "Wizard"

        if scr_x-10 > x > scr_x-110 \
                and 130 > y > 80:
            return "Archer"
        # other
        if 160 > x > 10 \
                and scr_y-10 > y > scr_y-70:
            return "exit"
        if scr_x-10 > x > scr_x-160 \
                and scr_y-10 > y > scr_y-70:
            return "next"

    # game mode
    if loc_id == 4:
        if 200 > x > 20 \
                and scr_y > y > scr_y-120:
            return "easy"
        if scr_x/2+90 > x > scr_x/2-90 \
                and scr_y > y > scr_y-120:
            return "medium"
        if scr_x-20 > x > scr_x-200 \
                and scr_y > y > scr_y-120:
            return "hard"

    # main game
    if loc_id == 9:
        if scr_x > x > scr_x-50 \
                and scr_y-50 > y > scr_y-100:
            return "setting"
        if scr_x/2 > x > scr_x/2-20 \
                and scr_y-50 > y > scr_y-100:
            return "allchat"
        if scr_x > x > scr_x-50 \
                and scr_y > y > scr_y-50:
            return "exit"
