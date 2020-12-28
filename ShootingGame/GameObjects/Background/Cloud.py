import random
from ..GameObject import GameObject


class Cloud(GameObject):
    def __init__(self, pygame, screen, image_file_name):
        GameObject.__init__(self, pygame, screen, image_file_name)
        self.set_position(0, screen.get_height() - self.get_height() * 0.5)
        self.save_position()
        self._x_inc = random.random()

    def determine_position(self):
        (x, y) = self.get_position()
        self.adjust_position_by_increment(self._x_inc)

        if x > self._screen.get_width():
            self.set_position(-self.get_width(), y)


