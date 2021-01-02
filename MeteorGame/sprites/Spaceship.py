from .Sprite import Sprite


class SpaceShip(Sprite):
    def __init__(self, screen, file_name, x_position, y_position):
        Sprite.__init__(self, screen, file_name, x_position, y_position)
        self._shield_surface = Sprite.load_image('shield.png')
        self._uncharged_image = self.image
        self._charged_image = Sprite.load_image('spaceship_charged.png')
        self.health = 5

    def update(self):
        self.rect.center = self._pygame.mouse.get_pos()
        self.apply_screen_constraints()
        self.draw_health()

    def draw_health(self):
        offset_y = self._shield_surface.get_height() / 2
        x_increment = self._shield_surface.get_width() + 10
        x_pos = 10

        for i in range(self.health):
            self._screen.blit(self._shield_surface, (x_pos, offset_y))
            x_pos += x_increment

    def reset_health(self):
        self.health = 5

    def collide(self, health_penalty):
        self.health -= health_penalty

    def charge(self):
        self.image = self._charged_image

    def discharge(self):
        self.image = self._uncharged_image

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
