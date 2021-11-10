import pygame
from random import randint
pygame.init

x_vin, y_vin = (800), (800)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()

Bilde = pygame.image.load("/Users/martinknutsen/opt/anaconda3/racecar.png")

x_kod_ball = 400
y_kod_ball = 400
x_kod_ball2 = 100
y_kod_ball2 = 100
radius = 50
radius_ball2 = 50
dx = 5
dy = 5
dx_aks = 1.0
R = 2.5
grader = 0


Bilde = pygame.transform.rotate(Bilde, grader)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)

    #pygame.draw.circle(vindu, farge_ball, (x_kod_ball, y_kod_ball), radius, width=0)
    vindu.blit(Bilde, (x_kod_ball, y_kod_ball))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_kod_ball -= dx
        if event.key == pygame.K_RIGHT:
            x_kod_ball += dx
            grader = 90
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
    pygame.display.flip()
    pygame.display.update()
