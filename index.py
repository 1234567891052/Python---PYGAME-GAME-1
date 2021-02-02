import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COL = (255, 255, 255)  # White
FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

pygame.display.set_caption("PYGAME TUTORIAL - SIMPLE 2 PLAYER GAME")


def draw(red, yellow):
    WIN.fill(BACKGROUND_COL)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    yellow = pygame.Rect((WIDTH) / 4, HEIGHT/2 - SPACESHIP_HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect((3 * WIDTH) / 4, HEIGHT/2 - SPACESHIP_HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(red, yellow)


if __name__ == "__main__":
    main()
