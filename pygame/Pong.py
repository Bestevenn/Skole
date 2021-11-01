import pygame
from random import randint
pygame.init

x_vin, y_vin = (1920),(1080)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120 
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()

x_kod_ball = 960
y_kod_ball = 540
radius = 50 
dx = 5
dy = 5
R = 2.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)
    pygame.draw.circle(vindu, farge_ball, (x_kod_ball, y_kod_ball), radius, width=0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_kod_ball -= dx
        if event.key == pygame.K_RIGHT:
            x_kod_ball += dx
        if event.key == pygame.K_UP:
            y_kod_ball -= dy
        if event.key == pygame.K_DOWN:
            y_kod_ball += dy
        if x_kod_ball > x_vin + radius:
            x_kod_ball = 0 - radius
        if x_kod_ball < 0 - radius:
            x_kod_ball = 1920 + radius
        
        if y_kod_ball > y_vin + radius:
            y_kod_ball = 0 - radius
        if y_kod_ball < 0 - radius:
            y_kod_ball = 1080 + radius




        if event.key == pygame.K_HOME:
            farge_ball = (randint(1,255), randint(1,255), randint(1,255))
        if event.key == pygame.K_TAB:
            radius += R
        if event.key == pygame.K_DELETE:
            radius -= R
        if radius > x_vin/2 or radius < 0:
            radius = 50

    pygame.display.update()