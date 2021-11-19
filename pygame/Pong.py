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

x_kod_rekkert = 800 - 100
y_kod_rekkert = 400
dx = 5
dy = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    vindu.fill(backgrunn)
    vindu.blit(Bilde, (x_kod_rekkert, y_kod_rekkert))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y_kod_rekkert -= dy
        if event.key == pygame.K_DOWN:
            y_kod_rekkert += dy
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

    pygame.display.update()
