import pygame
import os 




pygame.init()

Grå = (30, 30, 30)
GRØNN = (124,252,0)
SOL = (255,255,0)
brun = (139,69,19)
vindu = pygame.display.set_mode((1000, 1000))
white =(255, 255, 255) 

clock = pygame.time.Clock()


FPS = 120

x = 150
y = 0
dx = 15
dy = 15


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
    vindu.fill(Grå)
    pygame.draw.circle(vindu, SOL, (x,y), 10, width=0)

    y += dy
    x += dx
    if x == 1000 and y == 1000:
        y = 0
        x = 0

    print(x,y)
    
    pygame.display.update()