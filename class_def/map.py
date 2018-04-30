from pygame import image

class Map:
    tile_w = 40 # pixels
    tile_h = 40 # pixels
    def __init__(self, game):
        self.game = game
        self.surf = game.surf
        self.img = image.load('images/ground_square.png')
        screen_w, screen_h = self.surf.get_size()
        self.pos = (screen_w/2 - self.tile_w/2, screen_h/2 - self.tile_h/2)
        self.adjuster = {'left': (self.tile_w, 0),
            'right': (-self.tile_w, 0),
            'up': (0, self.tile_h),
            'down': (0, -self.tile_h)}
        self.target_pos = None

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
