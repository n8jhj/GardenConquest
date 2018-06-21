class Gnome:
    def __init__(self, game):
        self.game = game
        self.orientation = 'down'
        self.move_dir = None
        self.speed = 0.4

    def move(self, direction):
        self.orientation = direction
        self.move_dir = direction
        # self.game.set_target_position(direction)
