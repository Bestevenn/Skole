import pygame


import math
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
x_kod_ball2 = 300
y_kod_ball2 = 300
radius = 50
dx_aks = 1.0
R = 2.5
grader = 0
fart = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)

    pygame.draw.circle(vindu, farge_ball, (x_kod_ball,
                       y_kod_ball), radius, width=0)
    pygame.draw.circle(vindu, farge_ball, (x_kod_ball,
                       y_kod_ball), radius, width=0)

    pygame.display.update()
