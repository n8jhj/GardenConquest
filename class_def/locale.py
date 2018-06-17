class Locale:
    def __init__(self, map, center):
        self.map = map
        self.center = center
        self.tiles = self.map_query(center)

    def map_query(self):
        pass

    def draw(self):
        for tile in self.tiles:
            tile.draw()
