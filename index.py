import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COL = (222, 222, 222)  # White
FPS = 60

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT) 
BORDER_COLOR = (0, 0, 0) 

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACESHIP_VEL = 5 

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
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER) 
    pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] : #left
        yellow.x -= SPACESHIP_VEL
    if keys_pressed[pygame.K_d] : #right
        yellow.x += SPACESHIP_VEL
    if keys_pressed[pygame.K_w] : #up
        yellow.y -= SPACESHIP_VEL
    if keys_pressed[pygame.K_s] : #down
        yellow.y += SPACESHIP_VEL

def red_movement(keys_pressed, red) :
    if keys_pressed[pygame.K_LEFT] : #left
        red.x -= SPACESHIP_VEL
    if keys_pressed[pygame.K_RIGHT] : #right
        red.x += SPACESHIP_VEL
    if keys_pressed[pygame.K_UP] : #up
        red.y -= SPACESHIP_VEL
    if keys_pressed[pygame.K_DOWN] : #down
        red.y += SPACESHIP_VEL

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
        
        keys_pressed = pygame.key.get_pressed() 
        yellow_movement(keys_pressed, yellow) 
        red_movement(keys_pressed, red) 
        draw(red, yellow)

if __name__ == "__main__":
    main()
