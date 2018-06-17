from config.tileset import tile_imgs

class Tile:
    def __init__(self, map, type, pos):
        self.surf = map.surf
        self.img = tile_imgs[type]
        self.pos = pos

    def draw(self):
        self.surf.blit(self.img, self.pos)
