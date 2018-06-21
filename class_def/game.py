from class_def.event_handler import EventHandler
from class_def.artist import Artist
from class_def.gnome import Gnome

class Game:
    def __init__(self, surf):
        self.is_going = True
        self.handler = EventHandler(self)
        self.artist = Artist(surf, self)
        self.gnome = Gnome(self)

    def update(self):
        self.handler.handle()
        return self.is_going

    def draw(self):
        self.artist.draw()

    def set_target_position(self, direction):
        pass

    def move_up(self):
        self.gnome.move('up')

    def move_down(self):
        print('down')

    def move_left(self):
        print('left')

    def move_right(self):
        print('right')

    def quit(self):
        self.is_going = False
