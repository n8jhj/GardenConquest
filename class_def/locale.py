from config.screen import TILE_W, TILE_H

class Locale:
    def __init__(self, map, center):
        self.map = map
        self.center = center
        self.game = self.map.game
        self.surf = self.game.surf
        screen_w, screen_h = self.surf.get_size()
        self.pos = (screen_w/2 - TILE_W/2, screen_h/2 - TILE_H/2)
        self.adjuster = {'left': (TILE_W, 0),
            'right': (-TILE_W, 0),
            'up': (0, TILE_H),
            'down': (0, -TILE_H)}
        self.target_pos = None
        # self.tiles = self.map_query(center)

    def map_query(self, center):
        top_left = (center[0] - 1, center[1] - 1)
        top_right = (center[0] + 1, center[1] + 1)
        return self.map.tile_area(top_left, top_right)

    def draw(self):
        for tile in self.tiles:
            tile.draw()

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
