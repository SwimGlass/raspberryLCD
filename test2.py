import RPi.GPIO as GPIO
import time
import math
import pygame


def show(pin):
    if GPIO.input(pin):
        return 1
    else:
        return 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(32, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(36, GPIO.IN)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#rectangle = ([poizion(x,y)],[size(x,y)))
size = [300, 200]
rect7 = (200,20,20,20)
rect8 = (200,40,20,20)
rect9 = (200,60,20,20)
rect10 = (200,80,20,20)

title = "Hello, Pygame!"
pygame.init()

if e.type is KEYDOWN and e.key == K_w:
    screen = pygame.display.set_mode(size)
if e.type is KEYDOWN and e.key == K_f:
    screen = pygame.display.set_mode(size, FULLSCREEN)
#screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

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
pin10Time = 0
pinBuf = "0"
pinOn = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000
        buf= str(minutes) + " : " + str(seconds) 
        label = myfont.render(buf, 1, (255,255,0))
        #else:
        #    label = myfont.render(buf, 1, BLUE)
        x = (size[0]-label.get_width()) / 2
        y = (size[1]-label.get_height()) - 20 
        center = (size[1]-label.get_height()) / 2
        screen.fill(BLACK)
        
        a = (((math.pi/2-(math.pi*2)/60)+math.pi*2)%(math.pi*2))-seconds*math.pi*2/60
        b = ((math.pi/2+math.pi*2)%(math.pi*2))

        if b > a:
            pygame.draw.arc(screen,WHITE,(0,0,300,200),a,b,10)
        if a > b:
            pygame.draw.arc(screen,WHITE,(0,0,300,200),b,a,10)

        if show(35):
            pinOn = 1
            if show(29):
                countPin7+=1
                pinBuf = str(countPin7)
#            else:
#                countPin8+=1
#                pinBuf = str(countPin8)
        elif pinOn == 1:
            pinOn = 0
            countPin8+=1
            pinBuf = str(countPin8)
        if show(32) != 1:
            if show(33):
                pin10count +=1
            else:
                pin10count = 0
        if pin10count > 0:
            pygame.draw.rect(screen,RED,rect7)
            if pin10count > 1:
                pygame.draw.rect(screen,WHITE,rect8)
                if pin10count > 2:
                    pygame.draw.rect(screen,GREEN,rect9)
                    if pin10count > 3:
                        pygame.draw.rect(screen,BLUE,rect10)
        label1 = confont.render(pinBuf,1,WHITE)
        screen.blit(label1, (x,center))
        
        screen.blit(label, (x, y))
        pygame.display.flip()
        
#        print ("{}:{}".format(minutes, seconds))
    if seconds > 58:
        minutes += 1
        seconds -= 60
        stat = (stat + 1) % 3
    milliseconds += clock.tick_busy_loop(60)

GPIO.cleanup()
pygame.quit()
