import math
import pygame
from random import randint
pygame.init

x_vin, y_vin = (1280), (720)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()

Bilde = pygame.image.load("/Users/martinknutsen/opt/anaconda3/racecar.png")
bane = pygame.image.load("/Users/martinknutsen/opt/anaconda3/track2.png")

# fargegjennkjenning

midtfarge = (0, 0, 0, 255)


x_kod_ball = 110
y_kod_ball = 400
radius = 50
dx_aks = 1.0
R = 2.5
grader = 180
fart = 0.001


def tegnfigur(vindu1, fig, punkt, vinkel):
    rotertbilde = pygame.transform.rotate(fig, vinkel)
    x = punkt[0]
    y = punkt[1]
    vindu1.blit(rotertbilde, rotertbilde.get_rect(
        center=fig.get_rect(center=(x, y)).center).topleft)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)

    vindu.blit(bane,(0,0))

    #pygame.draw.circle(vindu, farge_ball, (x_kod_ball, y_kod_ball), radius, width=0)
    key = pygame.key.get_pressed()
    # Test for pil ned
    if key[pygame.K_LEFT]:
        grader += 3
        # Test for pil opp
    elif key[pygame.K_RIGHT]:
        grader -= 3
    elif key[pygame.K_ESCAPE]:
        pygame.quit()
    elif key[pygame.K_UP]:
        fart += 0.1
    elif key[pygame.K_DOWN]:
        fart -= 0.1

    x_kod_ball += fart*math.sin(grader*math.pi/180)
    y_kod_ball += fart*math.cos(grader*math.pi/180)

    if x_kod_ball > x_vin + radius:
        x_kod_ball = 0 - radius
    if x_kod_ball < 0 - radius:
        x_kod_ball = 1280 + radius
    if y_kod_ball > y_vin + radius:
        y_kod_ball = 0 - radius
    if y_kod_ball < 0 - radius:
        y_kod_ball = 720 + radius
    

    # fargegjennkjennig
    farge = bane.get_at((640,360))
    
    if 


    tegnfigur(vindu, Bilde, (x_kod_ball, y_kod_ball), grader)
    pygame.display.flip()
    clock.tick(fps)

