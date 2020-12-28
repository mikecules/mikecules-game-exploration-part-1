from ..GameObject import GameObject


class CrossHair(GameObject):
    def animate(self):
        (x, y) = self.get_pygame().mouse.get_pos()
        self.set_position(x, y)
        self.get_screen().blit(self.get_surface(), self.get_rect(center=(x, y)))
