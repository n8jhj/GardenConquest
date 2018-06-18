from pygame.constants import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_q)
from pygame import display
from colors import BLACK
from class_def.gnome import Gnome
from class_def.map import Map
from class_def.locale import Locale

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
        self.map = Map(self)
        locale_center = (1, 1)
        self.locale = Locale(self.map, locale_center)
        self.gnome = Gnome(self)
        self.can_interact = True

    def update(self):
        '''Update game state'''
        self.locale.update()
        if self.can_interact:
            for key in self.pressed:
                if self.pressed[key]:
                    self.key_function[key]()
        return self.is_going

    def draw(self):
        '''Draw the game window'''
        self.surf.fill(BLACK)
        self.locale.draw()
        self.gnome.draw()
        display.update()

    def key_action(self, key, press):
        '''Perform action related to pressed key'''
        self.pressed[key] = press

    # _____________KEY_PRESS_FUNCTIONS_____________

    def move_up(self):
        self.gnome.move('up')
        self.can_interact = False

    def move_down(self):
        self.gnome.move('down')
        self.can_interact = False

    def move_left(self):
        self.gnome.move('left')
        self.can_interact = False

    def move_right(self):
        self.gnome.move('right')
        self.can_interact = False

    def quit_game(self):
        self.is_going = False
