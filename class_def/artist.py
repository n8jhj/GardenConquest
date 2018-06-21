from config.colors import BLACK
from config.images import (RED_GNOME_ORTN_IMG, GNOME_IMG_SIZE,
    GNOME_IMG_HEIGHT_ADJUST)

class Artist:
    def __init__(self, surface, game):
        self.surf = surface
        self.game = game
        self.gnome_draw_pos = self.calc_gnome_draw_pos()

    def draw(self):
        self.surf.fill(BLACK)
        self.draw_gnome()
    
    def draw_gnome(self):
        gnome_orientation = self.game.gnome.orientation
        gnome_img = RED_GNOME_ORTN_IMG[gnome_orientation]
        self.surf.blit(gnome_img, self.gnome_draw_pos)

    def calc_gnome_draw_pos(self):
        return (self.surf.get_width() / 2 - GNOME_IMG_SIZE[0] / 2,
            self.surf.get_height() / 2 - GNOME_IMG_SIZE[1] / 2 \
            - GNOME_IMG_SIZE[1] * GNOME_IMG_HEIGHT_ADJUST)
