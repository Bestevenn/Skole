import pygame
from random import randint
pygame.init


hvit = (255, 255, 255)
x_vin, y_vin = (800, 800)
FPS = 200
klokke = pygame.time.Clock()
rød = (randint(0,255),randint(0,255), randint(0,255))
backgrunn = (30, 30, 30)

vindu = pygame.display.set_mode((x_vin, y_vin))


radius = 20
x_pos, y_pos = 200, 200

dx = 2
dy = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(backgrunn)
    klokke.tick(FPS)
 
    pygame.draw.circle(vindu, rød, (x_pos, y_pos), radius, width=0)
    def lageball():
        pygame.draw.circle(vindu, rød, (x_pos - randint(0, 600), y_pos - randint(0,600)), radius, width=0)

    x_pos += dx
    y_pos += dy
    if x_pos > 800 - radius:
        dx = -dx
    if y_pos > 800 - radius:
        dy = -dy
    if x_pos < 0 + radius:
        dx = -dx
    if y_pos < 0 + radius:
        dy = -dy
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if dx and dy < 0:
                print
            else:
                dx += 1
                dy += 1
        if event.key == pygame.K_DOWN:
            dx -= 1
            dy -= 1
            if dy < 0:
                dx = 2
                dy = 1
        if event.key == pygame.K_RIGHT:
            lageball()
        if event.key == pygame.K_ESCAPE:
            pygame.quit
    print(dx, dy, x_pos, y_pos)
    pygame.display.update()

