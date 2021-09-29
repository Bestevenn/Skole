import pygame 
import time

pygame.init()

HIMMELBLA = (25, 25, 25)
GRØNN = (124,252,0)
SUN = (255,255,0)
brun = (139,69,19)
vindu = pygame.display.set_mode((400, 400))
white =(255, 255, 255) 

clock = pygame.time.Clock()



pygame.display.update()

x = 200
y = 200
dx = 1
dy = 1
timer = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        clock.tick(timer)
        vindu.fill(HIMMELBLA)
        pygame.draw.circle(vindu, SUN, (x,y), 50, width=0)
        #x += dx
        y += dy
        pygame.display.update()
        



    