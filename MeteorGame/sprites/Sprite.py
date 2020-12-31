import pygame
import os


class Sprite(pygame.sprite.Sprite):
    ASSETS_DIR = '{0}/assets/img'.format(os.getcwd())

    def __init__(self, screen, file_name, x_position, y_position):
        pygame.sprite.Sprite.__init__(self)
        self._pygame = pygame
        self._screen = screen
        self.image = pygame.image.load('{0}/{1}'.format(Sprite.ASSETS_DIR, file_name))
        self.rect = self.image.get_rect(center=(x_position, y_position))

    def apply_screen_constraints(self):
        pass

