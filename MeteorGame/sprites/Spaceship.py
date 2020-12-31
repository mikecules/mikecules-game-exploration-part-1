from .Sprite import Sprite


class SpaceShip(Sprite):
    def __init__(self, screen, file_name, x_position, y_position, speed):
        Sprite.__init__(self, screen, file_name, x_position, y_position)

    def update(self):
        self.rect.center = self._pygame.mouse.get_pos()
        self.apply_screen_constraints()

    def apply_screen_constraints(self):
        screen_width = self._screen.get_width()
        screen_height = self._screen.get_height()

        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        elif self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        elif self.rect.top <= 0:
            self.rect.top = 0
