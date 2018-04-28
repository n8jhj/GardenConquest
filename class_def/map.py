from pygame import image

class Map:
    tile_w = 40 # pixels
    tile_h = 40 # pixels
    def __init__(self, surf):
        self.surf = surf
        self.img = image.load('images/ground_square.png')

    def draw(self):
        screen_w, screen_h = self.surf.get_size()
        pos = (screen_w/2 - self.tile_w/2, screen_h/2 - self.tile_h/2)
        self.surf.blit(self.img, pos)
