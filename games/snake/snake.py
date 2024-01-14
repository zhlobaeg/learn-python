import pygame

class Snake:
    def __init__(self, surface, x, y):
        self.x = x
        self.y = y
        self.surface = surface
        self.color = (0, 255, 51)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x + 1, self.y + 1, 38, 38))