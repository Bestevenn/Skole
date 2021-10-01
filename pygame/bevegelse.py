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




x = 150
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
    Fortsett = True
    while Fortsett:
        if x < 300 and y < 150:
            x += dx
            y += dy
        elif x == 300 and y == 150:
           Fortsett = False 
    if x == 300 and y == 150:
    x -= dx
    y += dy
    print(x,y)


    pygame.display.update()