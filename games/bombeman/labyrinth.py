import pygame

class Labyrinth:

    def __init__(self, color):
        self.color = color

    def draw(self, surface):
        step = 40
        x = 0
        y = surface.get_height()
        while x < surface.get_width():
            pygame.draw.line(surface, self.color, (x, 0), (x, y))
            x += step

        y = 0
        x = surface.get_width()
        while y < surface.get_height():
            pygame.draw.line(surface, self.color, (0, y), (x, y))
            y += step