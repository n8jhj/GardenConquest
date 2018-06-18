from config.images import (RED_GNOME_UP, RED_GNOME_DN, RED_GNOME_LT,
    RED_GNOME_RT, GNOME_IMG_SIZE, GNOME_IMG_HEIGHT_ADJUST)

class Gnome:
    img_up = RED_GNOME_UP
    img_dn = RED_GNOME_DN
    img_lt = RED_GNOME_LT
    img_rt = RED_GNOME_RT
    ortn_img = {
        'up': img_up,
        'down': img_dn,
        'left': img_lt,
        'right': img_rt
    }
    img_size = GNOME_IMG_SIZE
    height_adjust = GNOME_IMG_HEIGHT_ADJUST

    def __init__(self, game, orient='down', velocity=0.4):
        self.game = game
        self.surf = game.surf
        self.orientation = orient
        self.velocity = velocity
        self.draw_pos = (self.surf.get_width() / 2 - self.img_size[0] / 2,
            self.surf.get_height() / 2 - self.img_size[1] / 2 \
            - self.img_size[1] * self.height_adjust)
        self.move_dir = None

    def draw(self):
        self.surf.blit(self.ortn_img[self.orientation], self.draw_pos)

    def orient(self, orientation):
        self.orientation = orientation

    def move(self, dir):
        self.orient(dir)
        self.move_dir = dir
        self.set_locale_target_position(dir)

    def set_locale_target_position(self, dir):
        self.game.locale.set_target_pos(dir)
