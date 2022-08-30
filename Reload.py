from pygame import *
from GameSprite import *
import time as timer

old_time = 0
reload = dict()

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()