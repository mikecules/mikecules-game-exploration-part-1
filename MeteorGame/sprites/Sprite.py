import pygame
import os


class Sprite(pygame.sprite.Sprite):
    ASSETS_DIR = '{0}/assets/img'.format(os.getcwd())
    SURFACE_CACHE = {}

    def __init__(self, screen, file_name, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self._pygame = pygame
        self._screen = screen

        image_file_path = '{0}/{1}'.format(Sprite.ASSETS_DIR, file_name)

        if image_file_path not in Sprite.SURFACE_CACHE:
            Sprite.SURFACE_CACHE[image_file_path] = pygame.image.load(image_file_path)

        self.image = Sprite.SURFACE_CACHE[image_file_path]
        self.rect = self.image.get_rect(center=(x_position, y_position))

    def apply_screen_constraints(self):
        pass

