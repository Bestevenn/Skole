import math
import pygame
from random import randint
from time import sleep
pygame.init


pygame.display.set_caption("Bilspill")
x_vin, y_vin = (1280), (720)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()
green = (0, 255, 0)
blue = (0, 0, 128)



Bilde = pygame.image.load("/Users/martinknutsen/opt/anaconda3/racecar.png")
bane = pygame.image.load("/Users/martinknutsen/opt/anaconda3/track2.png")


start_x = 110 
start_y = 400

x_kod_ball = start_x
y_kod_ball = start_y
radius = 50
dx_aks = 1.0
R = 2.5
grader = 180
fart = 0.001


# teller og tekst

treff = 0

def tegnfigur(vindu1, fig, punkt, vinkel):
    rotertbilde = pygame.transform.rotate(fig, vinkel)
    x = punkt[0]
    y = punkt[1]
    vindu1.blit(rotertbilde, rotertbilde.get_rect(
        center=fig.get_rect(center=(x, y)).center).topleft)

test = 50

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

    if x_kod_ball > x_vin - radius - test:
        x_kod_ball = x_vin - radius - test
    if x_kod_ball < 0 - radius + test:
        x_kod_ball = 0 - radius + test
    if y_kod_ball > y_vin - radius: 
        y_kod_ball = y_vin - radius 
    if y_kod_ball < 0 - radius + test:
        y_kod_ball = 0 - radius + test

    # fargegjennkjennig
   
    
    farge_bil = bane.get_at((int(x_kod_ball), int(y_kod_ball)))
    
    if farge_bil == (255,38,0) or farge_bil == (50,124,11):
        treff += 1
        if treff == 5:
            x_kod_ball = start_x
            y_kod_ball = start_y
            fart = 0.001
            treff = 0 
        print("ani", "treff =", treff)
        
    else:
        print("tikk", "treff =", treff)


    tegnfigur(vindu, Bilde, (x_kod_ball, y_kod_ball), grader)
    pygame.display.flip()
    clock.tick(fps)

