import pygame

pygame.init()


hvit = (255, 255, 255)
x_vin, y_vin = (800, 800)
FPS = 200
klokke = pygame.time.Clock()

vindu = pygame.display.set_mode((x_vin, y_vin))


def car(x, y):

    Bilde = ("/Users/martinknutsen/Downloads/racecar.png")
    vis_bilde = pygame.image.load(Bilde)
    vindu.blit(vis_bilde, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
