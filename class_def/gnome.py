from pygame import image

class Gnome:
    img_up = image.load('images/gnome-ready/red_gnome_up.png')
    img_dn = image.load('images/gnome-ready/red_gnome_dn.png')
    img_lt = image.load('images/gnome-ready/red_gnome_lt.png')
    img_rt = image.load('images/gnome-ready/red_gnome_rt.png')
    ortn_img = {
        'up': img_up,
        'down': img_dn,
        'left': img_lt,
        'right': img_rt
    }
    img_size = (29, 45)
    height_adjust = 0.3

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
        self.set_map_target_position(dir)

    def set_map_target_position(self, dir):
        self.game.map.set_target_pos(dir)
