from .Sprite import Sprite
import random


class Meteor(Sprite):
    def __init__(self, screen, file_name, x_position, y_position, x_speed, y_speed):
        Sprite.__init__(self, screen, file_name, x_position, y_position)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        x1, y1 = self.rect.center
        x2 = x1 + self.x_speed
        y2 = y1 + self.y_speed
        self.rect.center = (x2, y2)
        self.apply_screen_constraints()

    def apply_screen_constraints(self):
        screen_width = self._screen.get_width()
        screen_height = self._screen.get_height()
        width = self.image.get_width()
        height = self.image.get_height()

        if self.rect.left >= screen_width:
            self.rect.right = 0
        elif self.rect.right <= 0:
            self.rect.left = screen_width + width /2

        if self.rect.top >= screen_height:
            self.rect.bottom = -height / 2

