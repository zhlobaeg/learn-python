import pygame

BRICK_SIZE = 40

class Brick:

    def __init__(self, x, y, color):
        self.x = x 
        self.y = y
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, BRICK_SIZE, BRICK_SIZE))