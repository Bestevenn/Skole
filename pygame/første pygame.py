import pygame 
import time

pygame.init()

HIMMELBLA = (25, 25, 25)
GRØNN = (124,252,0)
SUN = (255,255,0)
brun = (139,69,19)
white =(255, 255, 255) 
clock = pygame.time.Clock()
vindu = pygame.display.set_mode((400, 400))





x = 200
y = 200
dx = 1
dy = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        vindu.fill(HIMMELBLA)

        pygame.draw.circle(vindu, SUN, (x,y), 5)
        y += dy
        
        clock.tick(10)
        pygame.display.update()


        



    