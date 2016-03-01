import pygame
import sys
import math

GRAY = (220,220,221)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
size = [300, 200]
#rect1 = (10,0,(size[0]-20)/2,10)
#rect2 = ((size[0]-20)/2,0,(size[0]-10),10)
#rect3 = (size[0]-10,0,size[0],size[1])
#rect4 = ((size[0]-20)/2,size[1]-10,(size[0]-10),size[1])
#rect5 = (10,size[1]-10,(size[0]-20)/2,size[1])
#rect6 = (0,0,10,size[1])
#circle1 = (10,10,10,0)
circle1 = [[55,171,226],[50,50],10,0]
circle2 = [[86,102,174],[35,70],10,0]
circle3 = [[40,158,147],[35,100],10,0]
circle4 = [[150,195,99],[50,120],10,0]
circle5 = (GRAY,[50,50],10,0)
circle6 = (GRAY,[35,70],10,0)
circle7 = (GRAY,[35,100],10,0)
circle8 = (GRAY,[50,120],10,0)
title = "Hello, Pygame!"
pygame.init()

screen = pygame.display.set_mode(size,0,32)

pygame.display.set_caption(title)
myfont = pygame.font.SysFont("comicsansms", 70)

clock = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0
stat = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000
        buf= str(minutes) + " : " + str(seconds) 
        if stat == 0:
            label = myfont.render(buf, 1, BLACK)
        if stat == 1:
            label = myfont.render(buf, 1, BLUE)
        if stat == 2:
            label = myfont.render(buf, 1, RED)
        x = (size[0]-label.get_width()) / 2
        y = (size[1]-label.get_height()) - 20
        screen.fill(WHITE)
        a = (((math.pi/2-(math.pi*2)/60)+math.pi*2)%(math.pi*2))-seconds*math.pi*2/60
        b = ((math.pi/2+math.pi*2)%(math.pi*2))
        #pygame.draw.arc(screen,WHITE,(5,5,280,280),(((math.pi/2-(math.pi*2)/60)+math.pi*2)%(math.pi*2))-seconds*math.pi*2/60,((math.pi/2+math.pi*2)%(math.pi*2))-seconds*math.pi*2/60,10)
        if b > a:
            pygame.draw.arc(screen,[200,200,200],(0,0,300,200),a,b,10)
        if a > b:
            pygame.draw.arc(screen,[200,200,200],(0,0,300,200),b,a,10)
#        pygame.draw.circle(screen,circle1)
#        pygame.draw.circle(screen,circle2)
#        pygame.draw.circle(screen,circle3)
#        pygame.draw.circle(screen,circle4)
        pygame.draw.circle(screen,[55,171,226],[50,50],10,0)#circle1
        pygame.draw.circle(screen,[86,102,174],[35,70],10,0)#circle2
        pygame.draw.circle(screen,[40,158,147],[35,100],10,0)#circle3
        pygame.draw.circle(screen,[40,158,147],[50,120],10,0)#circle4
#        pygame.draw.circle(screen,GRAY,[50,50],10,0)#circle1
#        pygame.draw.circle(screen,GRAY,[35,70],10,0)#circle2
#        pygame.draw.circle(screen,GRAY,[35,100],10,0)#circle3
#        pygame.draw.circle(screen,GRAY,[50,120],10,0)#circle4
#        if seconds > 2:
#            pygame.draw.rect(screen,WHITE,rect1)
#        if seconds > 4:
#            pygame.draw.rect(screen,RED,rect2)
#        if seconds > 6:
#            pygame.draw.rect(screen,GREEN,rect3)
#        if seconds > 8:
#            pygame.draw.rect(screen,RED,rect4)
#       if seconds > 10:
#            pygame.draw.rect(screen,WHITE,rect5)
#        if seconds > 12:
#            pygame.draw.rect(screen,GREEN,rect6)
        screen.blit(label, (x, y))
        pygame.display.flip()
        
#        print ("{}:{}".format(minutes, seconds))
    if seconds > 60:
        minutes += 1
        seconds -= 60
        stat = (stat + 1) % 3
    milliseconds += clock.tick_busy_loop(60)

pygame.quit()
