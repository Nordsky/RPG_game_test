import pygame
import pole_gener as pg
import setting as s

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

"""sc = pygame.display.set_mode((400, 300))

pygame.mixer.music.load('Test.mp3')
pygame.mixer.music.play()

sound1 = pygame.mixer.Sound('boom.wav')
sound2 = pygame.mixer.Sound('one.ogg')

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
                # pygame.mixer.music.stop()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                sound1.play()
            elif i.button == 3:
                sound2.play()
    pygame.time.delay(20)"""

step_1 = pygame.mixer.Sound('sounds/step_01.wav')


def check_sound(tile, back):
    if tile == 1:
        if back == 'b':
            step_1.set_volume(s.so_vol)
            step_1.play()
