"""
GARDEN CONQUEST

A game where players compete to make their gardens grow.
"""

import pygame

from config.screen import SCREEN_SIZE
from class_def.game import Game

# Set up pygame.
DISPSURF = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Garden Conquest')
pygame.init()

# Set up Clock.
FPS = 30
fpsClock = pygame.time.Clock()

# Set up Game, EventHandler, Artist.
gc_game = Game(DISPSURF)

def main():
    going = True
    
    while going:
        going = controllerTick() # event handling
        viewTick() # drawing
        fpsClock.tick(FPS) # clock

def controllerTick():
    return gc_game.update()

def viewTick():
    gc_game.draw()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        # sys.exit() #temporary
