import RPi.GPIO as GPIO
import time 
import pygame

def show(pin):
    if GPIO.input(pin):
        return 1
    else:
        return 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
size = [400, 300]
rect1 = (10,0,(size[0]-20)/2,10)
rect2 = ((size[0]-20)/2,0,(size[0]-10),10)
rect3 = (size[0]-10,0,size[0],size[1])
rect4 = ((size[0]-20)/2,size[1]-10,(size[0]-10),size[1])
rect5 = (10,size[1]-10,(size[0]-20)/2,size[1])
rect6 = (0,0,10,size[1])

title = "Hello, Pygame!"
pygame.init()

screen = pygame.display.set_mode((400,300),0,32)

pygame.display.set_caption(title)
myfont = pygame.font.SysFont("comicsansms", 70)
confont = pygame.font.SysFont("comicsansms",100)

clock = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0
stat = 0
countPin7 = 0
countPin8 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000
        buf= str(minutes) + " : " + str(seconds) 
        label = myfont.render(buf, 1, (255,255,0))
        label1 = myfont.render(buf, 1, (255,255,0))
        if show(7):
            countPin7+=1
            label1 = confont.render(str(countPin7),1,WHITE)
        if show(8):
            countPin8+=1
            label1 = confont.render(str(countPin8),1,BLUE)
        #else:
        #    label = myfont.render(buf, 1, BLUE)
        x = (size[0]-label.get_width()) / 2
        y = (size[1]-label.get_height()) - 20 
        center = (size[1]-label.get_height()) / 2
        screen.fill(BLACK)
        if seconds > 2:
            pygame.draw.rect(screen,WHITE,rect1)
        if seconds > 4:
            pygame.draw.rect(screen,RED,rect2)
        if seconds > 6:
            pygame.draw.rect(screen,GREEN,rect3)
        if seconds > 8:
            pygame.draw.rect(screen,RED,rect4)
        if seconds > 10:
            pygame.draw.rect(screen,WHITE,rect5)
        if seconds > 12:
            pygame.draw.rect(screen,GREEN,rect6)
        screen.blit(label, (x, y))
        screen.blit(label1, (x,center))
        pygame.display.flip()
        
#        print ("{}:{}".format(minutes, seconds))
    if seconds > 59:
        minutes += 1
        seconds -= 60
        stat = (stat + 1) % 3
    milliseconds += clock.tick_busy_loop(60)

GPIO.cleanup()
pygame.quit()
