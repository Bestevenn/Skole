import pygame 
import time

pygame.init()

HIMMELBLA = (135, 206, 235)
GRØNN = (124,252,0)
SUN = (255,255,0)
brun = (139,69,19)
vindu = pygame.display.set_mode((400, 300))
white =(255, 255, 255) 

clock = pygame.time.Clock()




x = 0
y = 150
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(10)
    vindu.fill(HIMMELBLA)
    pygame.draw.circle(vindu, SUN, (x,y), 10, width=0)
    x += 1
    pygame.draw.rect(vindu, GRØNN, (0,200,400,400), width=0)
    pygame.draw.polygon(vindu, brun, [(0,200),(50,100),(100,200)])
    pygame.draw.polygon(vindu, brun, [(100,200),(150,100),(200,200)])
    pygame.display.update()

