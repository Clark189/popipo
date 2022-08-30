from pygame import *
from GameSprite import GameSprite
from random import randint
from time import *

class Enemy(GameSprite):
    def update(self):
        self.rect_y += self.speed
        global lost
        if self.rect_y > self.speed:
            self.rect.x = randint(80, self.width - 80)
            self.rect_y = 0
            return 1
        return 0
