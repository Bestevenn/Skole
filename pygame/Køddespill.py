import math
import pygame
from random import randint
from time import sleep


bane_til_bilde = input("skriv banen til bildet: ")
bane_til_bil = input("skriv banen til bil: ")
print("min mac = 1 ")



pygame.init
pygame.font.init()

pygame.display.set_caption("Bilspill")
x_vin, y_vin = (1280), (720)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()
green = (0, 255, 0)
blue = (0, 0, 128)



if bane_til_bil and bane_til_bilde == "1":
    Bilde = pygame.image.load("/Users/martinknutsen/opt/anaconda3/racecar.png")
    bane = pygame.image.load("/Users/martinknutsen/opt/anaconda3/track2.png")
else:
    bilde = pygame.image.load(bane_til_bil)
    bane = pygame.image.load(bane_til_bilde)


start_x = 110 
start_y = 400

y_kod_bil = start_x
y_kod_bil = start_y
radius = 50
dx_aks = 1.0
R = 2.5
grader = 180
fart = 0.001


# teller og tekst

poeng_verdi = 0
font = pygame.font.SysFont('arial', 32)
x_font = 500
y_font = 500
def vis_poeng(x,y):
    poeng = font.render("Poeng : " + str(poeng_verdi),True,(255,255,255))
    vindu.blit(poeng,(x, y))


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
    #pygame.draw.circle(vindu, farge_ball, (y_kod_bil, y_kod_bil), radius, width=0)
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

    y_kod_bil += fart*math.sin(grader*math.pi/180)
    y_kod_bil += fart*math.cos(grader*math.pi/180)

    if y_kod_bil == x_vin - radius - test:
        y_kod_bil = x_vin - radius - test
    if y_kod_bil < 0 - radius + test:
        y_kod_bil = 0 - radius + test
    if y_kod_bil > y_vin + radius + test: 
        y_kod_bil = y_vin + radius + test
    if y_kod_bil < 0 - radius + test:
        y_kod_bil = 0 - radius + test

    # fargegjennkjennig
   
    farge = bane.get_at((400,400))
    farge_bil = bane.get_at((int(y_kod_bil), int(y_kod_bil)))
    
    if farge_bil == (255,38,0) or farge_bil == (50,124,11):
        poeng_verdi += 1
        if poeng_verdi == 5:
            y_kod_bil = start_x
            y_kod_bil = start_y
            fart = 0.001
            poeng_verdi = 0 
        print("ani", "poeng_verdi =", poeng_verdi)
        
    else:
        print("ikke ani", "poeng_verdi =", poeng_verdi)


    tegnfigur(vindu, Bilde, (y_kod_bil, y_kod_bil), grader)
    vis_poeng(x_font, y_font)
    pygame.display.flip()
    clock.tick(fps)

