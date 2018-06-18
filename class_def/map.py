from pygame import image
import configparser

class Map:
    def __init__(self, game):
        self.game = game
        self.surf = game.surf
        self.layout_file = 'config/test-map.txt'
        self.load()

    def load(self):
        '''Load the list of nodes.'''
        n_tiles_x = 3
        n_tiles_y = 3
        self.nodes = [[1]*n_tiles_x]*n_tiles_y
