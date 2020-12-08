import pygame
import sys
from time import sleep
pygame.init()
sonido=pygame.mixer.Sound(sys.argv[1])
sonido.play()
sleep(float(sys.argv[2]))
pygame.quit()