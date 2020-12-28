import os


class GameObject:
    CURRENT_DIR = os.getcwd()
    ASSET_DIR = '{0}/assets'.format(CURRENT_DIR)
    ASSET_IMG_DIR = '{0}/img'.format(ASSET_DIR)
    IMG_SURFACE_CACHE = {}

    @staticmethod
    def fetch_image_asset(pygame, file_name):
        file_path = '{0}/{1}'.format(GameObject.ASSET_IMG_DIR, file_name)

        if file_path not in GameObject.IMG_SURFACE_CACHE:
            GameObject.IMG_SURFACE_CACHE[file_path] = pygame.image.load(file_path)

        return GameObject.IMG_SURFACE_CACHE[file_path]

    def __init__(self, pygame, screen, image_file_name):
        self._pygame = pygame
        self._screen = screen
        self._image_asset_surface = GameObject.fetch_image_asset(pygame, image_file_name)
        self._xy_position = (0, 0)
        self._x_inc = 0
        self._y_inc = 0
        self._saved_xy_position = self._xy_position

    def get_pygame(self):
        return self._pygame

    def get_screen(self):
        return self._screen

    def get_height(self):
        return self._image_asset_surface.get_height()

    def get_width(self):
        return self._image_asset_surface.get_width()

    def get_surface(self):
        return self._image_asset_surface

    def get_rect(self, **kwargs):
        return self.get_surface().get_rect(**kwargs)

    def get_position(self):
        return self._xy_position

    def save_position(self):
        self._saved_xy_position = self.get_position()

    def get_saved_position(self):
        return self._saved_xy_position

    def set_position(self, x, y):
        self._xy_position = (x, y)
        return self._xy_position

    def adjust_position_by_increment(self, x_inc=0, y_inc=0):
        (x, y) = self._xy_position
        return self.set_position(x_inc + x, y_inc + y)

    def determine_position(self):
        pass

    def collide(self):
        pass

    def animate(self):
        self.determine_position()
        self._screen.blit(self.get_surface(), self.get_position())
