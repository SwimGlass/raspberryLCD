import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
size = [400, 300]
#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((400,300),0,32)

pygame.display.set_caption("Bouncing Rectangle")
done = False
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50

rect_change_x = 2
rect_change_y = 2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 250 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 350 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
