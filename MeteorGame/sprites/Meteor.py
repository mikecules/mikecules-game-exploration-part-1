from .Sprite import Sprite


class Meteor(Sprite):
    def __init__(self, screen, file_name, x_position, y_position, x_speed, y_speed):
        Sprite.__init__(self, screen, file_name, x_position, y_position)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.sprite_reused_count = 0

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
        updated = False

        if self.rect.left >= screen_width:
            self.rect.right = 0
            updated = True
        elif self.rect.right <= 0:
            self.rect.left = screen_width + width / 2
            updated = True

        if self.rect.top >= screen_height:
            self.rect.bottom = -height / 2
            updated = True

        if updated:
            self.sprite_reused_count += 1

