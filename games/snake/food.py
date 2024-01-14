import pygame
import random

def generate_coordinates():
        x = random.randint(0, 17) * 40
        y = random.randint(0, 17) * 40
        return (x, y)

class Food:
    def __init__(self,  surface):
        self.surface = surface
        (x, y) = generate_coordinates()
        self.x = x
        self.y = y
        self.color = (204, 0, 51)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x + 1, self.y + 1, 38, 38))
        