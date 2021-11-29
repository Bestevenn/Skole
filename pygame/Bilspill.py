import math
import pygame
from random import randint
from time import sleep
pygame.init
pygame.font.init()


print("skriv 1 på begge for mac")
bane_bilde = input("Skriv banen til bakgrunnen: ")
bane_bil = input("Skriv banen til bil: ")

pygame.display.set_caption("Bilspill")
x_vin, y_vin = (1280), (720)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()
green = (0, 255, 0)
blue = (0, 0, 128)


if bane_bilde and bane_bil == "1":
    Bilde = pygame.image.load("/Users/martinknutsen/opt/anaconda3/racecar.png")
    bane = pygame.image.load("/Users/martinknutsen/opt/anaconda3/track2.png")
else:
    bane = pygame.image.load(f"{bane_bilde}")
    Bilde = pygame.image.load(f"{bane_bil}")



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


poeng_verdi = 0
font = pygame.font.SysFont('arial', 32)
x_font = 600
y_font = 400
def vis_poeng(x,y):
    poeng = font.render("Poeng : " + str(poeng_verdi),True,(255,255,255))
    vindu.blit(poeng,(x, y))


def tegnfigur(vindu1, fig, punkt, vinkel):
    rotertbilde = pygame.transform.rotate(fig, vinkel)
    x = punkt[0]
    y = punkt[1]
    vindu1.blit(rotertbilde, rotertbilde.get_rect(
        center=fig.get_rect(center=(x, y)).center).topleft)

kant = 50

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

    if x_kod_ball > x_vin - radius - kant:
        x_kod_ball = x_vin - radius - kant
    if x_kod_ball < 0 - radius + kant:
        x_kod_ball = 0 - radius + kant
    if y_kod_ball > y_vin - radius: 
        y_kod_ball = y_vin - radius 
    if y_kod_ball < 0 - radius + kant:
        y_kod_ball = 0 - radius + kant

    # fargegjennkjennig
   
    
    farge_bil = bane.get_at((int(x_kod_ball), int(y_kod_ball)))
    

    if farge_bil == (255,38,0) or farge_bil == (50,124,11):
        poeng_verdi += 1
        if poeng_verdi >= 1:
            fart /= 2
        if poeng_verdi == 5:
            x_kod_ball = start_x
            y_kod_ball = start_y
            fart = 0.001
            poeng_verdi = 0 
        print("ani", "treff =", poeng_verdi)
        
    else:
        print("ikke ani", "treff =", poeng_verdi)

    vis_poeng(x_font, y_font)
    tegnfigur(vindu, Bilde, (x_kod_ball, y_kod_ball), grader)
    pygame.display.flip()
    clock.tick(fps)

