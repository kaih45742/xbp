import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/kai23/mygit/xbp/project1/ahiru.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)


