import pygame
import sys

pygame.init()

width,height = 300,300
size = width,height

black = 0,0,0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

color=(100,0,0)

pygame.draw.rect(screen,color,(50,50,200,200)

pygame.display.flip()
