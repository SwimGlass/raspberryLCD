import pygame

size = [300,200]
title = "Hello, Pygame!"
pygame.init()

screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption(title)
myfont = pygame.font.Font(None,60)
myfont = pygame.font.SysFont("comicsansms", 70)

GRAY = (220,220,221)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
end1 = 15
end2 = 30
end3 = 14
end4 = 3
e1 = end1
e2 = end2
e3 = end3
e4 = end4
rect1 = (20,150,50,2)
rect2 = (90,150,50,2)
rect3 = (160,150,50,2)
rect4 = (230,150,50,2)
while True:
    total1 = myfont.render(str(e1),True,WHITE)
    screen.blit(total1,(20,150))
    while end1 > 0:
        rect1 = (20,150-end1*2,50,2)
        pygame.draw.rect(screen,WHITE,rect1)
        end1 -= 1
    total2 = myfont.render(str(e2),1,WHITE)
    screen.blit(total2,(90,150))
    while end2 > 0:
        rect2 = (90,150-end2*2,50,2)
        pygame.draw.rect(screen,WHITE,rect2)
        end2 -= 1
    total3 = myfont.render(str(e3),1,WHITE)
    screen.blit(total3,(160,150))
    while end3 > 0:
        rect3 = (160,150-end3*2,50,2)
        pygame.draw.rect(screen,WHITE,rect3)
        end3 -= 1
    total4 = myfont.render(str(e4),1,WHITE)
    screen.blit(total4,(230,150))
    while end4 > 0:
        rect4 = (230,150-end4*2,50,2)
        pygame.draw.rect(screen,WHITE,rect4)
        end4 -= 1
    pygame.display.flip()

