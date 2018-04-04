"""
GARDEN CONQUEST

A game where players compete to make their gardens grow.
"""

import pygame, sys
from pygame.locals import *
import game

# set up pygame
SIZE = (750, 400)
DISPSURF = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Garden Conquest')
pygame.init()

# set up Clock
FPS = 30
fpsClock = pygame.time.Clock()

# set up game
main_game = game.Game(DISPSURF)

def main():
    going = True
    
    while going:
        going = controllerTick() # event handling
        viewTick() # drawing
        fpsClock.tick(FPS) # clock

def controllerTick():
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        if event.type == KEYDOWN:
            main_game.key_action(event.key, True)
        if event.type == KEYUP:
            main_game.key_action(event.key, False)
    return main_game.update()

def viewTick():
    main_game.draw()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        # sys.exit() #temporary
