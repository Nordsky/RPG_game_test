import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Grand adventure v 0.7")

def bl(screen):
    blank_surf = pygame.Surface((300, 400))
    blank_surf.fill((110, 110, 110))
    screen.blit(blank_surf, (0, 0))

clock = pygame.time.Clock()
FPS = 30
k = 0
x = 0
y = 0
lm = False
rm = False
fff = []
def gif_check():
    fff.clear()
    for i in range(6):
        fff.append(pygame.image.load('gif/fire_1/f' + str(i+1) + '.png'))
        print(fff[i])

def fired(screen, x):
    global k
    if x == 6:
        k = 0
        x = 0
    bl(screen)
    fire = pygame.image.load(fff[x])
    screen.blit(fire, (0, 0))

gif_check()
bl(screen)
#fire = pygame.image.load(fff[0])
#screen.blit(fire, (0, 0))

pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    lm = True
                if e.button == 3:
                    rm = True

        if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    lm = False
                if e.button == 3:
                    rm = False

    #fired(screen, k)
    if lm == True:
        x -= 5
    if rm == True:
        x += 5
    k += 1
    #print(k)
    if k >= 18:
        k = 0
    bl(screen)
    screen.blit(fff[k//3], (x, y))
    pygame.display.update()
    clock.tick(FPS)

















    
