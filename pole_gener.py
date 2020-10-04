import pygame
import setting as s
import player as p
import monster as mo

wall = pygame.image.load('loc/tiles/forest/wall_1.jpg')
ground_1 = pygame.image.load('loc/tiles/forest/grass_1.jpg')
ground_2 = pygame.image.load('loc/tiles/forest/stone_panel_1.jpg')
ground_3 = pygame.image.load('loc/tiles/forest/wood_panel_1.jpg')
water = pygame.image.load('loc/tiles/forest/water_1.jpg')
decor_1 = pygame.image.load('loc/tiles/forest/crate_1.jpg')
decor_2 = pygame.image.load('loc/tiles/forest/wood_spil_1.png')
door_1 = pygame.image.load('loc/tiles/forest/door_1.png')
door_vert = pygame.image.load('loc/tiles/forest/door_vert_1.jpg')
down = pygame.image.load('loc/tiles/forest/down_1.jpg')

night = pygame.image.load('loc/tiles/night_1.jpg')
light = pygame.image.load('loc/tiles/light_1.png')

montile = mo.rand_monster

tile = 1
surf = pygame.Surface((1600, 900))
surf.fill((0, 0, 0))
loc_trans = []      # ids loc from transport

path_first = 'loc/location/start_loc.txt'
a = []          # main mas
f = open(path_first)
m = len(f.readlines())      # len file
f.seek(0)
for li in f:
    a.append(li)
x = int(a[m-5])
y = int(a[m-4])
day_night = 8
f.close()
"""print("id location: " + a[m-1])
print("id region: " + a[m-2])
print("name: " + a[m-3])
print("y: " + a[m-4])
print("x: " + a[m-5])
print("loc count: " + a[m-6])
print("tile name: " + a[m-7])

for i in range(m-7-int(a[m-6]), m-7):
    print(a[i])

for i in range(int(a[m-4])):
    print(a[i])

for i in range(int(a[m-4])+1, int(a[m-4])*2+1):
    print(a[i])

for i in range(int(a[m-4])*2+2, int(a[m-4])*3+2):
    print(a[i])

for i in range(int(a[m-4])*3+3, int(a[m-4])*4+3):
    print(a[i])"""
n = []


# paint dark or light
def sun_moon(i, px, py):
    global n
    n.clear()
    if i == 0:
        n.clear()
        for v in range(y):
            n.append([])
            for j in range(x):
                n[v].append(0)
    if i == 1:
        n.clear()
        for v in range(y):
            flag = True
            n.append([])
            for j in range(x):
                if v == py-2 and j == px:
                    n[v].append(2)
                    flag = False
                if v == py-1 and (j == px - 1 or j == px or j == px + 1):
                    n[v].append(2)
                    flag = False
                if v == py and (j == px - 2 or
                                j == px - 1 or
                                j == px or
                                j == px + 1 or
                                j == px + 2):
                    n[v].append(2)
                    flag = False
                if v == py+1 and (j == px - 1 or j == px or j == px + 1):
                    n[v].append(2)
                    flag = False
                if v == py+2 and j == px:
                    n[v].append(2)
                    flag = False
                if flag:
                    n[v].append(1)
                flag = True
    if i == 2:
        n.clear()
        for v in range(y):
            flag = True
            n.append([])
            for j in range(x):
                if v == py-3 and j == px:
                    n[v].append(2)
                    flag = False
                if v == py-2 and (j == px - 1 or j == px or j == px + 1):
                    n[v].append(2)
                    flag = False
                if v == py-1 and (j == px - 2 or
                                j == px - 1 or
                                j == px or
                                j == px + 1 or
                                j == px + 2):
                    n[v].append(2)
                    flag = False
                if v == py and (j == px - 3 or
                                j == px - 2 or
                                j == px - 1 or
                                j == px or
                                j == px + 1 or
                                j == px + 2 or
                                j == px + 3):
                    n[v].append(2)
                    flag = False
                if v == py+1 and (j == px - 2 or
                                j == px - 1 or
                                j == px or
                                j == px + 1 or
                                j == px + 2):
                    n[v].append(2)
                    flag = False
                if v == py+2 and (j == px - 1 or j == px or j == px + 1):
                    n[v].append(2)
                    flag = False
                if v == py+3 and j == px:
                    n[v].append(2)
                    flag = False
                if flag:
                    n[v].append(1)
                flag = True
    # for i in range(y):
        # print(n[i])

# sun_moon(1, 5, 3)
# for i in range(y):
#     print(n[i])


# check id all loc for transport of this loc
def check_loc_id():
    global loc_trans
    global day_night
    day_night = 8
    loc_trans.clear()
    for i in range(int(a[m-6])):
        loc_trans.append(a[m-8-i])
        day_night += 1


def check_light():
    global day_night
    return int(a[m-day_night])

    
# check id this loc
def change_loc(path):
    global path_first
    if path == '0001' or path == 1:
        return 'loc/location/test_loc.txt'
    if path == '0002' or path == 2:
        return 'loc/location/first_dungeon.txt'
    if path == '0003' or path == 3:
        return 'loc/location/start_loc.txt'
    if path == '0004' or path == 4:
        return 'loc/location/podval_tavern.txt'
    if path == '9999' or path == 9999:
        return 'loc/location/blank.txt'


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# check id this loc tile set
def check_tile(name):
    if name == 'forest':
        print("yea")
        return 1

    
# download tiles from this loc tile set
def check_loc(path):
    global a
    global m
    global loc_trans
    global tile
    loc_path = change_loc(path)
    file = open(loc_path)
    m = len(file.readlines())
    file.seek(0)
    a.clear()
    for k in file:
        a.append(k)
    check_loc_id()
    global x
    global y
    x = int(a[m - 5])
    y = int(a[m - 4])
    global wall
    global ground_1
    global ground_2
    global ground_3
    global water
    global decor_1
    global decor_2
    global door_1
    global door_vert
    global down
    for g in range(x):      # x
        for j in range(y+1, y*2+1):      # y
            if a[j][g] == 'p':
                p.pos_y = j-y-1
                p.pos_x = g
    tile = check_tile(a[m - 7])
    if tile == 1:
        print("2")
        wall = pygame.image.load('loc/tiles/forest/wall_1.jpg')
        ground_1 = pygame.image.load('loc/tiles/forest/stone_panel_1.jpg')
        ground_2 = pygame.image.load('loc/tiles/forest/grass_1.jpg')
        ground_3 = pygame.image.load('loc/tiles/forest/wood_panel_1.jpg')
        water = pygame.image.load('loc/tiles/forest/water_1.jpg')
        decor_1 = pygame.image.load('loc/tiles/forest/crate_1.jpg')
        decor_2 = pygame.image.load('loc/tiles/forest/wood_spil_1.png')
        door_1 = pygame.image.load('loc/tiles/forest/door_1.png')
        door_vert = pygame.image.load('loc/tiles/forest/door_vert_1.jpg')
        down = pygame.image.load('loc/tiles/forest/down_1.jpg')

    # paint_back(screen)
    file.close()


# paint 1 lvl background
def paint_back(screen):
    global x
    global y
    for g in range(x):      # x
        for j in range(y):      # y
            if a[j][g] == 'b':
                screen.blit(ground_1, (g * s.sot, j * s.sot))
            if a[j][g] == 'w':
                screen.blit(wall, (g * s.sot, j * s.sot))
            if a[j][g] == '1':
                screen.blit(ground_2, (g * s.sot, j * s.sot))
            if a[j][g] == '2':
                screen.blit(ground_3, (g * s.sot, j * s.sot))
            if a[j][g] == '3':
                screen.blit(water, (g * s.sot, j * s.sot))


# paint 2 lvl location
def paint_door(screen):
    global x
    global y
    for g in range(x):      # x
        for j in range(y+1, y*2+1):      # y
            if a[j][g] == '2':
                screen.blit(down, (g * s.sot, (j-y-1) * s.sot))
            if a[j][g] == '5':
                screen.blit(door_1, (g * s.sot, (j-y-1) * s.sot))
            if a[j][g] == '3':
                screen.blit(down, (g * s.sot, (j-y-1) * s.sot))
            if a[j][g] == '6':
                screen.blit(door_1, (g * s.sot, (j-y-1) * s.sot))            


# paint 3 lvl location
def paint_decor(screen):
    global x
    global y
    for g in range(x):      # x
        for j in range(y*2+2, y*3+2):      # y
            if a[j][g] == '1':
                screen.blit(decor_1, (g * s.sot, (j-y*2-2) * s.sot))
            if a[j][g] == '2':
                screen.blit(decor_2, (g * s.sot, (j-y*2-2) * s.sot))


# paint 4 lvl location
def paint_monster(screen):
    global x
    global y
    for g in range(x):      # x
        for j in range(y*3+3, y*4+3):      # y
            if a[j][g] == '1':
                screen.blit(montile, (g * s.sot, (j-y*3-3) * s.sot))
            if a[j][g] == '2':
                screen.blit(decor_2, (g * s.sot, (j-y*3-3) * s.sot))


# paint 5 lvl location
def paint_night(screen):
    global x
    global y
    global n
    for g in range(x):      # x
        for j in range(y):      # y
            if n[j][g] == 1:
                screen.blit(night, (g * s.sot, j * s.sot))
            if n[j][g] == 2:
                screen.blit(light, (g * s.sot, j * s.sot))


# do player go to new location ?
def trans_loc(sc, nx, ny):
    global loc_trans
    global a
    if a[ny][nx] == '2' or a[ny][nx] == '5':
        sc.blit(surf, (0, 0))
        check_loc(int(loc_trans[0]))
        s.co_back = True
        s.co_text = True
    if a[ny][nx] == '3' or a[ny][nx] == '6':
        sc.blit(surf, (0, 0))
        check_loc(int(loc_trans[1]))
        s.co_back = True
        s.co_text = True


# player not move
def no_move(nx, ny, key):
    global a
    if a[ny][nx] == 'w' or a[ny][nx] == '3':
        if key == 1:
            p.pos_y += 1
        if key == 2:
            p.pos_y -= 1
        if key == 3:
            p.pos_x += 1
        if key == 4:
            p.pos_x -= 1
        p.key = 0
    else:
        p.key = 1
    if a[ny+y*2 + 2][nx] == '2':
        if key == 1:
            p.pos_y += 1
        if key == 2:
            p.pos_y -= 1
        if key == 3:
            p.pos_x += 1
        if key == 4:
            p.pos_x -= 1
        p.key = 0
    else:
        p.key = 1


# paint player
def paint_player(screen):
    global x
    global y
    global a
    play_ico = p.player_stand_pic
    for g in range(x):      # x
        for j in range(y):      # y
            if p.player_pos[j][g] == '1':
                screen.blit(play_ico, (g * s.sot, j * s.sot))
