import math
import pygame
pygame.init
pygame.mixer.init



def stoppe():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

x_vin, y_vin = (800), (800)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
hvit = (255, 255, 255)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()
kod_bakke = (0,500,800,800)

def bakke(kod):
    pygame.draw.rect(vindu, hvit, (kod), width=0)

# ball eller blokk 1
radius = 50 
y_kod_ball = 500 - radius + 1
x_kod_ball = 600
radius2 = radius/2
# ball eller blokk 2
radius2 = radius
y_kod_ball2 = 500 - radius2 + 1
x_kod_ball2 = 200

n = 5
Ball_masse1 = 100*n
ball_masse2 = 1 


dx = 1
dx2 = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)
    bakke(kod_bakke)
    pygame.draw.circle(vindu, farge_ball, (x_kod_ball, y_kod_ball), radius, width=0)
    pygame.draw.circle(vindu, (160,30,188), (x_kod_ball2, y_kod_ball2), radius2, width=0)

    x_kod_ball += -dx
    x_kod_ball2 += dx2
    if x_kod_ball == x_kod_ball2 + radius*2:

        dx = -dx
        dx2 = -dx2
    if x_kod_ball2 < 0 + radius:
        dx2 = -dx2
    if x_kod_ball > x_vin - radius:
        dx = -dx
    
    print("xkod1 = ", x_kod_ball, "xkod2 =", x_kod_ball2)
    
    stoppe()
    pygame.display.update()
    clock.tick(fps)

