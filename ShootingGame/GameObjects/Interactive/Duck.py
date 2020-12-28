from ..GameObject import GameObject


class Duck(GameObject):

    def animate(self):
        self.determine_position()
        centered_rect = self.get_rect(topleft=self.get_position())
        self._screen.blit(self.get_surface(), centered_rect)
