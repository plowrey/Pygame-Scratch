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

shipImg = pygame.image.load(r'C:\Codebase\Pictures\spaceship.png')
shipImg = pygame.transform.scale(shipImg, (100, 100))

background = pygame.image.load(r'C:\Codebase\Pictures\background.jpg')
background = pygame.transform.scale(background, (700, 500))
window.blit(background, (0, 0))

FPS = 30
clock = pygame.time.Clock()

x, y = 300, 400
MOVE_UP = 4
MOVE_DOWN = 3
MOVE_RIGHT = 2
MOVE_LEFT = 1
direction = 0

# loop to keep window open until quit
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = MOVE_LEFT
            elif event.key == K_RIGHT:
                direction = MOVE_RIGHT
            elif event.key == K_UP:
                direction = MOVE_UP
            elif event.key == K_DOWN:
                direction = MOVE_DOWN

    if direction == MOVE_LEFT:
        x -= 0.05
    elif direction == MOVE_RIGHT:
        x += 0.05
    elif direction == MOVE_UP:
        y -= 0.05
    elif direction == MOVE_DOWN:
        y += 0.05

    window.blit(shipImg, (x, y))
    pygame.display.update()
    pygame.display.flip()
