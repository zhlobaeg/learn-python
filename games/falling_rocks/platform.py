import pygame
import enum

class Direction(enum.Enum):
    left = 1
    right = 2

class Platform:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.prev_x = self.x
        self.prev_y = self.y
        self.color = (72, 128, 64)
        self.step = 19
        self.width = 76
        self.high = 38
        self.direction = None

    def save_pos(self):
        self.prev_x = self.x
        self.prev_y = self.y

    def moving(self):
        if self.direction == Direction.left:
            self.step_left()
        elif self.direction == Direction.right:
            self.step_right()

    
    def step_left(self):
        if self.x - self.step >= 0: 
            self.save_pos()
            self.x -= self.step

    def step_right(self):
        if self.x + self.width < self.surface.get_width():
            self.save_pos()
            self.x += self.step

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x + 1, self.y + 1, self.width, self.high))


    def check_hit(self, stone):
        if self.y >= stone.y and self.y <= (stone.y + stone.high):
            if self.x <= (stone.x + stone.width) and (self.x + self.width) >= stone.x:
                return True
        return False