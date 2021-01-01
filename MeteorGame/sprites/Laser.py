from .Sprite import Sprite


class Laser(Sprite):
    def __init__(self, screen, file_name, x_position, y_position, speed):
        Sprite.__init__(self, screen, file_name, x_position, y_position)
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed

        if self.rect.bottom <= 0:
            self.kill()


