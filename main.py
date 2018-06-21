"""
GARDEN CONQUEST

A game where players compete to make their gardens grow.
"""

import pygame, sys

from config.screen import SCREEN_SIZE
import game
import artist

# Set up pygame.
DISPSURF = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Garden Conquest')
pygame.init()

# Set up Clock.
FPS = 30
fpsClock = pygame.time.Clock()

# Set up Game and Artist.
gc_game = game.Game()
gc_artist = artist.Artist(DISPSURF, gc_game)

def main():
    going = True
    
    while going:
        going = controllerTick() # event handling
        viewTick() # drawing
        fpsClock.tick(FPS) # clock

def controllerTick():
    return True

def viewTick():
    pass

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        # sys.exit() #temporary
