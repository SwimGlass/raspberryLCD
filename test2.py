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
GPIO.setup(38, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(32, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(36, GPIO.IN)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (220,220,221)
#rectangle = ([poizion(x,y)],[size(x,y)))
size = [500, 300]
rect7 = (200,30,20,20)
rect8 = (200,55,20,20)
rect9 = (200,80,20,20)
rect10 = (200,105,20,20)

title = "Hello, Pygame!"
pygame.init()

screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

img = "img1.png"
image = pygame.image.load(img).convert()
screen.blit(image,(0,0))
pygame.display.update()
time.sleep(3)

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
countPin9 = 0
countPin10 = 0
pin10Time = 0
pinBuf = " "
pinOn = 0
pin36count = 0
pin10count = 0
flag = 0
count30 = 0
mode = 0
buf= str(minutes) + " : " + str(seconds) 
label = myfont.render(buf, 1, BLACK)

def p():
    if b > a:
        pygame.draw.arc(screen,GRAY,(0,0,300,200),a,b,10)
    if a > b:
        pygame.draw.arc(screen,GRAY,(0,0,300,200),b,a,10)
    if stat == 0:
        pygame.draw.circle(screen,[55,171,226],[50,50],10,0)
        pygame.draw.circle(screen,[86,102,174],[35,70],10,0)
        pygame.draw.circle(screen,[40,158,147],[35,100],10,0)
        pygame.draw.circle(screen,[150,195,99],[50,120],10,0)
    if stat == 1:
        pygame.draw.circle(screen,[55,171,226],[50,50],10,0)
        pygame.draw.circle(screen,GRAY,[35,70],10,0)
        pygame.draw.circle(screen,GRAY,[35,100],10,0)
        pygame.draw.circle(screen,GRAY,[50,120],10,0)
    if stat == 2:
        pygame.draw.circle(screen,GRAY,[50,50],10,0)
        pygame.draw.circle(screen,[86,102,174],[35,70],10,0)
        pygame.draw.circle(screen,GRAY,[35,100],10,0)
        pygame.draw.circle(screen,GRAY,[50,120],10,0)
    if stat == 3:
        pygame.draw.circle(screen,GRAY,[50,50],10,0)
        pygame.draw.circle(screen,GRAY,[35,70],10,0)
        pygame.draw.circle(screen,[40,158,147],[35,100],10,0)
        pygame.draw.circle(screen,GRAY,[50,120],10,0)
    if stat == 4:
        pygame.draw.circle(screen,GRAY,[50,50],10,0)
        pygame.draw.circle(screen,GRAY,[35,70],10,0)
        pygame.draw.circle(screen,[40,158,147],[35,100],10,0)
        pygame.draw.circle(screen,GRAY,[50,120],10,0)
    label1 = confont.render(pinBuf,1,BLACK)
    buf= str(minutes) + " : " + str(seconds) 
    label = myfont.render(buf, 1, BLACK)
    screen.blit(label1, (center_x,center_y))    
    screen.blit(label, (x, y))

def total():
    end1 = countPin7
    end2 = countPin8
    end3 = countPin9
    end4 = countPin10
    total1 = myfont.render(str(countPin7),True,BLACK)
    screen.blit(total1,(20,150))
    while end1 > 0:
        rect1 = (20,150-end1*2,50,2)
        pygame.draw.rect(screen,BLACK,rect1)
        end1 -= 1
    total2 = myfont.render(str(countPin8),1,BLACK)
    screen.blit(total2,(90,150))
    while end2 > 0:
        rect2 = (90,150-end2*2,50,2)
        pygame.draw.rect(screen,BLACK,rect2)
        end2 -= 1
    total3 = myfont.render(str(countPin9),1,BLACK)
    screen.blit(total3,(160,150))
    while end3 > 0:
        rect3 = (160,150-end3*2,50,2)
        pygame.draw.rect(screen,BLACK,rect3)
        end3 -= 1
    total4 = myfont.render(str(countPin10),1,BLACK)
    screen.blit(total4,(230,150))
    while end4 > 0:
        rect4 = (230,150-end4*2,50,2)
        pygame.draw.rect(screen,BLACK,rect4)
        end4 -= 1
 
   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    
    if milliseconds > 1000:
        seconds += 1
        count30 += 1
        if count30 >= 30:
            Break = 2
        else:
            Break = 0
        milliseconds -= 1000
        buf= str(minutes) + " : " + str(seconds) 
        label = myfont.render(buf, 1, BLACK)
        #else:
        #    label = myfont.render(buf, 1, BLUE)
        x = (size[0]-label.get_width()) / 2
        y = (size[1]-label.get_height()) - 20 
        center_x = 110
        center_y = 50
        screen.fill(WHITE)
        
        a = (((math.pi/2-(math.pi*2)/60)+math.pi*2)%(math.pi*2))-seconds*math.pi*2/60
        b = ((math.pi/2+math.pi*2)%(math.pi*2))
        if show(36):
            mode = 2
            pinOn = 1
            if show(38):
                count30 = 0
                pinOn = 0
                countPin7+=1
                pinBuf = str(countPin7)
                stat = 1
            elif show(35):
                count30 = 0
                pinOn = 0
                pin36count += 1
#            else:
#                countPin8+=1
#                pinBuf = str(countPin8)
        if mode == 2 and pinOn == 1 and show(36)==0:
            mode = 1
        if mode != 2:
            if pinOn == 1:
                pinOn = 0
                countPin8+=1
                pinBuf = str(countPin8)
                stat = 2
        if show(32) != 1:
            stat = 3
            if show(33):
                count30 = 0
                flag += 1
                pin10count +=1
            elif flag >= 1:
                countPin9 += 1
                pinBuf = str(countPin9)
                flag = 0
            else:
                pin10count = 0
        else:
            flag = 0
        if pin10count > 0:
            pygame.draw.rect(screen,[185,191,218],rect7)
            if pin10count > 1:
                pygame.draw.rect(screen,[185,191,218],rect8)
                if pin10count > 2:
                    pygame.draw.rect(screen,[185,191,218],rect9)
                    if pin10count > 3:
                        pygame.draw.rect(screen,[185,191,218],rect10)
        elif pin36count >= 2:
            countPin10+=1
            pin36count = 0
            pinBuf = str(countPin10)
            stat = 4
        if Break != 2:
            p()
        else:
            total()
        pygame.display.flip()
        
#        print ("{}:{}".format(minutes, seconds))
    if seconds > 58:
        minutes += 1
        seconds -= 60
    milliseconds += clock.tick_busy_loop(60)

GPIO.cleanup()
pygame.quit()
