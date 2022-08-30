from pygame import *

def Bullet(GameSprite):
    def update(self):
        self.rect_y += self.speed
        if self.rect_y < 0:
            self.kill()