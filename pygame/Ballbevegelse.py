import pygame
pygame.init()

window_w = 800
window_h = 600

white = (255, 255, 255)
black = (0, 0, 0)

FPS = 240

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Game: ")
clock = pygame.time.Clock()


def game_loop():

    block_size = 20

    velocity = [1, 1]

    pos_x = window_w/2
    pos_y = window_h/2

    running = True

    radius = 32

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos_x += velocity[0]
        pos_y += velocity[1]

        if pos_x + block_size > window_w or pos_x < 0:
            velocity[0] = -velocity[0]

        if pos_y + block_size > window_h or pos_y < 0:
            velocity[1] = -velocity[1]

        # DRAW
        window.fill(white)
        pygame.draw.circle(window, black, (pos_x, pos_y), radius, width=0)
        pygame.display.update()
        clock.tick(FPS)
        print(pos_x, pos_y, "radius: ", radius)


game_loop()
