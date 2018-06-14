from pygame import image
import configparser

from config.tileset import tileset

class Map:
    tile_w = 40 # pixels
    tile_h = 40 # pixels
    def __init__(self, game):
        self.game = game
        self.surf = game.surf
        self.layout_file = 'config/test-map.txt'
        self.tileset = tileset
        screen_w, screen_h = self.surf.get_size()
        self.pos = (screen_w/2 - self.tile_w/2, screen_h/2 - self.tile_h/2)
        self.adjuster = {'left': (self.tile_w, 0),
            'right': (-self.tile_w, 0),
            'up': (0, self.tile_h),
            'down': (0, -self.tile_h)}
        self.target_pos = None
        self.setup()

    def setup(self):
        # look into self.layoutFile and load the proper Tiles
        layout = []
        map_key = {}
        parser = configparser.ConfigParser()
        parser.read(self.layout_file)
        layout = parser.get('map', 'layout').split('\n')
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                map_key[section] = desc
        self.width = len(layout[0]) # 10
        self.height = len(layout) # 6
        self.tiles = [None]*self.width*self.height
        for i in range(self.height):
            for j in range(self.width):
                sym = layout[i][j]
                name = map_key[sym]['name']
                img = map_key[sym]['img']
                imgVis = map_key[sym]['img_vis']
                mvbl = map_key[sym]['moveable']
                mvbl = mvbl == 'True' or mvbl == 'true' or mvbl == '1' \
                       or mvbl == 'Yes' or mvbl == 'yes'
                sebl = map_key[sym]['seeable']
                sebl = sebl == 'True' or sebl == 'true' or sebl == '1' \
                       or sebl == 'Yes' or sebl == 'yes'
                self.tiles[i*self.width+j] = Tile(self, (j,self.height-i-1), \
                                                  name, img, imgVis, mvbl, sebl)

    def update(self):
        '''Update tile positions'''
        if self.gnome_is_moving():
            dir = self.gnome_move_dir()
            gnome_vel = self.gnome_velocity()
            self.pos = (self.pos[0] + self.adjuster[dir][0] * gnome_vel,
                self.pos[1] + self.adjuster[dir][1] * gnome_vel)
            if self.target_pos_reached():
                self.pos = self.target_pos
                self.stop_gnome_movement()
                self.set_game_interaction(True)

    def draw(self):
        self.surf.blit(self.img, self.pos)

    def set_target_pos(self, dir):
        self.target_pos = (self.pos[0] + self.adjuster[dir][0],
            self.pos[1] + self.adjuster[dir][1])

    def target_pos_reached(self):
        dir = self.gnome_move_dir()
        if dir == 'left':
            return self.pos[0] >= self.target_pos[0]
        elif dir == 'right':
            return self.pos[0] <= self.target_pos[0]
        elif dir == 'up':
            return self.pos[1] >= self.target_pos[1]
        elif dir == 'down':
            return self.pos[1] <= self.target_pos[1]

    def set_game_interaction(self, bool_val):
        self.game.can_interact = bool_val

    def gnome_velocity(self):
        '''The game's gnome velocity'''
        return self.game.gnome.velocity

    def gnome_move_dir(self):
        '''The direction in which the gnome is moving'''
        return self.game.gnome.move_dir

    def gnome_is_moving(self):
        '''Whether the game's gnome is moving'''
        return not self.game.gnome.move_dir == None

    def stop_gnome_movement(self):
        self.game.gnome.move_dir = None
