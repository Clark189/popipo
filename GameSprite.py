from curses import window
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y, win_width, win_hight, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = size_x
        self.rect.y = size_y
        self.width = win_width
        self.hight = win_hight
        self.window = window

        self.image = transform.scale(image.load(player_image), (size_x, size_y))

    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))