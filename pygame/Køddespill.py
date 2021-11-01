import pygame
from random import randint
pygame.init

x_vin, y_vin = (800), (800)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()

x_kod_ball = 400
y_kod_ball = 400
x_kod_ball2 = 100
y_kod_ball2 = 100
radius = 50
radius_ball2 = 50
dx = 5
dy = 5
R = 2.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)
    pygame.draw.circle(vindu, farge_ball, (x_kod_ball,
                       y_kod_ball), radius, width=0)
    pygame.draw.circle(vindu, farge_ball, (x_kod_ball2,
                       y_kod_ball2), radius, width=0)
    x_kod_ball2 += 1
    y_kod_ball2 += 1
    if x_kod_ball2 > x_vin + radius:
        x_kod_ball2 -= dx
    if x_kod_ball2 < x_vin - radius:
        x_kod_ball2 += dx
    if y_kod_ball2 > y_vin + radius:
        y_kod_ball2 -= dy
    if y_kod_ball2 < y_vin - radius:
        y_kod_ball2 += dx
    print(y_kod_ball2)
    print(x_kod_ball2)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_kod_ball -= dx
        if event.key == pygame.K_RIGHT:
            x_kod_ball += dx
        if event.key == pygame.K_UP:
            y_kod_ball -= dy
        if event.key == pygame.K_DOWN:
            y_kod_ball += dy
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
        if x_kod_ball > x_vin + radius:
            x_kod_ball = 0 - radius
        if x_kod_ball < 0 - radius:
            x_kod_ball = 800 + radius
        if y_kod_ball > y_vin + radius:
            y_kod_ball = 0 - radius
        if y_kod_ball < 0 - radius:
            y_kod_ball = 800 + radius
        if event.key == pygame.K_HOME:
            farge_ball = (randint(1, 255), randint(1, 255), randint(1, 255))
        if event.key == pygame.K_TAB:
            radius += R
        if event.key == pygame.K_DELETE:
            radius -= R
        if radius > x_vin/2 or radius < 0:
            radius = 50

    pygame.display.update()
