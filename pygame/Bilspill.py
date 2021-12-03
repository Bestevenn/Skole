import math
import pygame
from random import randint
from time import sleep
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
kant = 50



Bilde = pygame.image.load("/Users/martinknutsen/opt/anaconda3/racecar.png")
bane = pygame.image.load("/Users/martinknutsen/opt/anaconda3/track3.jpeg")




start_x = 110 
start_y = 400
radius = 50
dx_aks = 1.0
R = 2.5
grader = 180
x_kod_ball = start_x
y_kod_ball = start_y
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


#checkpoints

checkpoint_nr1,checkpoint_nr1_kod_x,checkpoint_nr1_kod_y,checkpoint_nr1_grader = (234,125,69),(250),(100),(90)
checkpoint_nr2, checkpoint_nr2_kod_x, checkpoint_nr2_kod_y,checkpoint_nr2_grader = (125,70,234),(881),(169),(144)
checkpoint_nr3, checkpoint_nr3_kod_x, checkpoint_nr3_kod_y, checkpoint_nr3_grader = (70,179,235),(1164),(255),(-6)
checkpoint_nr4,checkpoint_nr4_kod_x, checkpoint_nr4_kod_y, checkpoint_nr4_grader = (225,70,236),(620),(660),(-90)
status_checkpoint = 0


# sarte på nytt
def start_nytt(pros_x, pros_y,antall_grader):
    global x_kod_ball
    global y_kod_ball
    global fart
    global poeng_verdi
    global grader
    x_kod_ball = pros_x
    y_kod_ball = pros_y
    fart = 0.001
    poeng_verdi = 0 
    grader = antall_grader


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
        grader += 2
        # Test for pil opp
    elif key[pygame.K_RIGHT]:
        grader -= 2
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
    
    if farge_bil == checkpoint_nr1:
        status_checkpoint = 1
    elif farge_bil == checkpoint_nr2:
        status_checkpoint = 2
    elif farge_bil == checkpoint_nr3:
        status_checkpoint = 3
    elif farge_bil == checkpoint_nr4:
        status_checkpoint = 4

    
    print(status_checkpoint,"kordinater=", x_kod_ball, y_kod_ball)
    print("grader=", grader)
    if farge_bil == (69,235,125) or farge_bil == (50,124,11):
        poeng_verdi += 1
        if poeng_verdi >= 1:
            fart /= 1.1112
    
        
        if poeng_verdi == 100:
            if status_checkpoint == 0:
                start_nytt(start_x, start_y,180)        
            elif status_checkpoint == 1:
                start_nytt(checkpoint_nr1_kod_x, checkpoint_nr1_kod_y,checkpoint_nr1_grader)
            elif status_checkpoint == 2:
                start_nytt(checkpoint_nr2_kod_x,checkpoint_nr2_kod_y,checkpoint_nr2_grader)
            elif status_checkpoint == 3:
                start_nytt(checkpoint_nr3_kod_x,checkpoint_nr3_kod_y,checkpoint_nr3_grader)
            elif status_checkpoint == 4:
                start_nytt(checkpoint_nr4_kod_x,checkpoint_nr4_kod_y,checkpoint_nr4_grader)
        
     

    vis_poeng(x_font, y_font)
    tegnfigur(vindu, Bilde, (x_kod_ball, y_kod_ball), grader)
    pygame.display.flip()
    clock.tick(fps)


