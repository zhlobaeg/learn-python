import pygame
import enum

class Direction(enum.Enum):
    left = 1
    right = 2
    up = 3
    down = 4

class Snake:
    def __init__(self, surface, x, y):
        self.x = x
        self.y = y
        self.surface = surface
        self.direction = Direction.right
        self.color = (0, 255, 51)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x + 1, self.y + 1, 38, 38))

    def move(self):
        step = 40
        if self.direction == Direction.right:
            self.x += step
            if self.x >= self.surface.get_width():
                self.x = 0
        elif self.direction == Direction.left:
            self.x -= step
            if self.x < 0:
                self.x = self.surface.get_width()
        elif self.direction == Direction.up:
            self.y -= step
            if self.y < 0:
                self.y = self.surface.get_height()
        elif self.direction == Direction.down:
            self.y += step
            if self.y >= self.surface.get_height():
                self.y = 0