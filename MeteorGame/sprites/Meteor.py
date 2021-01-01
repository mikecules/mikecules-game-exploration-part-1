from .Sprite import Sprite
import random


class Meteor(Sprite):
    def __init__(self, screen, file_name, x_position, y_position, x_speed, y_speed):
        Sprite.__init__(self, screen, file_name, x_position, y_position)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.sprite_reused_count = 0
        self.original_image = self.image.copy()
        self.z_rotate_speed = min(0.1, random.random()) if random.randrange(0, 2) > 0 else max(-0.1, -random.random())
        self.current_z_angle = 0
        self.max_reuse_count = 0

    def rotate(self, x, y):
        z_angle = self.current_z_angle + self.z_rotate_speed

        if z_angle >= 360:
            z_angle -= 360
        elif z_angle <= -360:
            z_angle += 360

        self.image = self._pygame.transform.rotate(self.original_image, self.current_z_angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.current_z_angle = z_angle

    def update(self):
        x1, y1 = self.rect.center
        x2 = x1 + self.x_speed
        y2 = y1 + self.y_speed

        self.rotate(x2, y2)

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

            if self.sprite_reused_count > self.max_reuse_count:
                print('Killing meteor at count {0}'.format(self.sprite_reused_count - 1))
                self.kill()
