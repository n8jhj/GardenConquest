from pygame import image

RED_GNOME_UP = image.load('images/gnome-ready/red_gnome_up.png')
RED_GNOME_DN = image.load('images/gnome-ready/red_gnome_dn.png')
RED_GNOME_LT = image.load('images/gnome-ready/red_gnome_lt.png')
RED_GNOME_RT = image.load('images/gnome-ready/red_gnome_rt.png')
RED_GNOME_ORTN_IMG = {
    'up':       RED_GNOME_UP,
    'down':     RED_GNOME_DN,
    'left':     RED_GNOME_LT,
    'right':    RED_GNOME_RT,
}
GNOME_IMG_SIZE = (29, 45)  # pixels
GNOME_IMG_HEIGHT_ADJUST = 0.3  # multiplier
