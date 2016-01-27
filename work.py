import pygame
import time

size = [400, 300]
black = (0, 0, 0)
white = (255, 255, 255)
title = "Hello, Pygame!"

pygame.init()

screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption(title)
myfont = pygame.font.SysFont("comicsansms", 100)

time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    


    label = myfont.render(str(time), 1, (255,255,0))
    time.delay(1000)
    time += 1

    x = (size[0]-label.get_width()) / 2
    y = (size[1]-label.get_height()) / 2
    
    screen.fill(black)
   # screen.blit(label, (100, 100))
    screen.blit(label, (x, y))
    pygame.display.update()

pygame.quie()
