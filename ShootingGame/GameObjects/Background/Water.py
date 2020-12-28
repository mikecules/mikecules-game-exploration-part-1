from ..GameObject import GameObject


class Water(GameObject):
    def __init__(self, pygame, screen, image_file_name):
        GameObject.__init__(self, pygame, screen, image_file_name)
        self.set_position(0, screen.get_height() - self.get_height() * 0.5)
        self.save_position()
        self._y_inc = 0.5

    def determine_position(self):
        height = self.get_height()
        max_offset = height * 0.1
        (ox, oy) = self.get_saved_position()
        (x, y) = self.get_position()
        dy = y - oy

        if dy >= max_offset or dy <= -max_offset:
            self._y_inc = -self._y_inc

        self.adjust_position_by_increment(0, self._y_inc)


