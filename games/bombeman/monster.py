import pygame

class Monster:
    def __init__(self, surface, x, y):
        self.x = x
        self.y = y
        self.step = 40
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, (255, 0, 0), (self.x + 20, self.y + 20), 20)