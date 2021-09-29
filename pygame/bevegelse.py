import pygame
import os 




pygame.init()

Grå = (30, 30, 30)
GRØNN = (124,252,0)
SOL = (255,255,0)
brun = (139,69,19)
vindu = pygame.display.set_mode((300, 300))
white =(255, 255, 255) 

clock = pygame.time.Clock()




x = 0
y = 0
dx = 15
dy = 15


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(10)
    vindu.fill(Grå)
    pygame.draw.circle(vindu, SOL, (x,y), 10, width=0)
    x += dx
    y += dy


    print(x, y)
    if x == 300 and y == 300:
        x -= dx
        y -= dy
    pygame.draw.circle(vindu, SOL, (x,y), 10, width=0)
    pygame.display.update()

