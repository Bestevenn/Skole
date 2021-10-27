import pygame

import random


pygame.init

x_vin, y_vin = (1200), (800)
backgrunn = (25, 25, 25)
hvit = (255, 255, 255)
vindu = pygame.display.set_mode((x_vin, y_vin))
FPS = 200
klokke = pygame.time.Clock()

radius = 25
x_kod_ball = 0
y_kod_ball = 0
dx = 1
dy = 1
dy_minus = -(dy)
dy_pluss = +(dy)

avstand = radius + 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    klokke.tick(FPS)
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)

    regnbue = (a, b, c)
    vindu.fill(hvit)
    pygame.draw.circle(vindu, regnbue, (x_kod_ball,
                       y_kod_ball), radius, width=0)
    x_kod_ball = x_vin/2
    y_kod_ball += dy
    radius += 1
    if y_kod_ball > 800 - radius:
        dy += dy_minus
    elif y_kod_ball < 0 + radius:
        dy += dy_pluss
    if radius > 1000:
        radius = 1

    print(radius)

    pygame.display.update()
