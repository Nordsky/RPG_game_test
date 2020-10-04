import pygame

def bl(screen):
    blank_surf = pygame.Surface((300, 400))
    blank_surf.fill((110, 110, 110))
    screen.blit(blank_surf, (0, 0))

k = 0
x = 0
y = 0
lm = False
rm = False
fff = []
z = []

# load gif's sprite
def gif_check():
    fff.clear()
    z.clear()
    for i in range(6):
        fff.append('gif/fire_1/f' + str(i+1) + '.png')
        z.append(pygame.image.load(fff[i]))


#bl(screen)
#fire = pygame.image.load(fff[0])
#screen.blit(fire, (0, 0))
