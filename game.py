from pygame.constants import *
from pygame import display
from colors import BLACK
from custom_sprite_group import CustomGroup

class Game:
    def __init__(self, surf):
        self.surf = surf
        self.is_going = True # whether the game is still going
        self.key_function = {
            K_UP:       self.move_forward,
            K_DOWN:     self.move_backward,
            K_q:        self.quit_game
        }
        self.pressed = {}
        self.sprites = CustomGroup()
        self.add_gnome()

    def update(self):
        '''Update game state'''
        for key in self.pressed:
            if self.pressed[key]:
                self.key_function[key]()
        return self.is_going

    def draw(self):
        '''Draw the game window'''
        self.surf.fill(BLACK)
        self.sprites.draw(self.surf)
        display.update()

    def key_action(self, key, press):
        '''Perform action related to pressed key'''
        self.pressed[key] = press

    def add_gnome(self):
        '''Add a gnome'''
        pass

    # _____________KEY_PRESS_FUNCTIONS_____________

    def move_forward(self):
        pass

    def move_backward(self):
        pass

    def quit_game(self):
        self.is_going = False
