from pygame.constants import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_q)
from pygame import display
from colors import BLACK
from class_def.gnome import Gnome

class Game:
    def __init__(self, surf):
        self.surf = surf
        self.is_going = True # whether the game is still going
        self.key_function = {
            K_UP:       self.move_up,
            K_DOWN:     self.move_down,
            K_LEFT:     self.move_left,
            K_RIGHT:    self.move_right,
            K_q:        self.quit_game
        }
        self.pressed = {}
        self.gnome = self.new_gnome()

    def update(self):
        '''Update game state'''
        for key in self.pressed:
            if self.pressed[key]:
                self.key_function[key]()
        return self.is_going

    def draw(self):
        '''Draw the game window'''
        self.surf.fill(BLACK)
        self.gnome.draw()
        display.update()

    def key_action(self, key, press):
        '''Perform action related to pressed key'''
        self.pressed[key] = press

    def new_gnome(self):
        '''Return a new gnome'''
        return Gnome(self.surf)

    # _____________KEY_PRESS_FUNCTIONS_____________

    def move_up(self):
        self.gnome.orient('up')

    def move_down(self):
        self.gnome.orient('down')

    def move_left(self):
        self.gnome.orient('left')

    def move_right(self):
        self.gnome.orient('right')

    def quit_game(self):
        self.is_going = False
