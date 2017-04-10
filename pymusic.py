# -* coding=utf-8 *-

import pygame,sys

# pygame.init()
# pygame.mixer.init()
# screen=pygame.display.set_mode([640,480])
# pygame.time.delay(1000)
# pygame.mixer.music.load("Chopin-waltz-in-a-minor.mp3")
# pygame.mixer.music.play()
# while 1:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()

from playsound import playsound
playsound('Chopin-waltz-in-a-minor.mp3', block = True)