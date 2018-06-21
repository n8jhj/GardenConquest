import pygame
from pygame.locals import *
from pygame.constants import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_q)

class EventHandler:
    def __init__(self, game):
        self.game = game
        self.key_function = {
            K_UP:       self.game.move_up,
            K_DOWN:     self.game.move_down,
            K_LEFT:     self.game.move_left,
            K_RIGHT:    self.game.move_right,
            K_q:        self.game.quit,
        }
        self.pressed = {}
        self.can_interact = True

    def handle(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game.quit()
            if event.type == KEYDOWN:
                self.key_event(event.key, True)
            if event.type == KEYUP:
                self.key_event(event.key, False)
        if self.can_interact:
            for key in self.pressed:
                if self.pressed[key]:
                    self.key_function[key]()

    def key_event(self, key, press):
        self.pressed[key] = press
