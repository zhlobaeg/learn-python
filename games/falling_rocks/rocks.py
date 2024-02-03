import pygame
import random

class Rock:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.width = 38
        self.high = 38
        self.x = x
        self.y = y
        self.step = 10
        self.i = None
        self.u = None
        self.color = (121, 81, 137)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x + 1, self.y + 1, self.width, self.high))

    def move(self):
        self.y += self.step
        if self.y >= self.surface.get_height():
            self.y = 0
        self.i = random.randint(1,15)
        if self.i == 12:
            self.u = random.randint(1,2)
            if self.u == 1:
                self.x += 38
            elif self.u == 2:
                self.x -= 38

    def random_spawn(self):
        self.x = random.randint(1,76)
        self.x = self.x * 10
        self.y = random.randint(1,10)
        self.y = self.y * self.high