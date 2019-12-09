import pygame
from pygame.locals import *
from sys import exit

# window size and color
pygame.init()
width = 700
height = 500
background_color = (0, 0, 0)

# displaying and naming window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ship Fight Game')

# loading ship image and scaling it to size
shipImg = pygame.image.load(r'C:\Codebase\Pictures\spaceship.png')
shipImg = pygame.transform.scale(shipImg, (100, 100))

# loading background image and fitting to screen
background = pygame.image.load(r'C:\Codebase\Pictures\background.jpg')
background = pygame.transform.scale(background, (700, 500))
window.blit(background, (0, 0))

# clock makes sure your game doesnt run to fast
clock = pygame.time.Clock()


x, y = 300, 400
MOVE_UP = 1
MOVE_DOWN = 2
MOVE_RIGHT = 3
MOVE_LEFT = 4
direction = 0

# loop to keep window open until quit
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        # Keydown looks for user to press a key
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = MOVE_LEFT
            elif event.key == K_RIGHT:
                direction = MOVE_RIGHT
            elif event.key == K_UP:
                direction = MOVE_UP
            elif event.key == K_DOWN:
                direction = MOVE_DOWN

    # moving the x or y of the ship depending on keyboard input
    if direction == MOVE_LEFT:
        x -= 0.05
    elif direction == MOVE_RIGHT:
        x += 0.05
    elif direction == MOVE_UP:
        y -= 0.05
    elif direction == MOVE_DOWN:
        y += 0.05

    # blit is printing images to the window every frame.
    window.blit(shipImg, (x, y))
    pygame.display.update()
    pygame.display.flip()
