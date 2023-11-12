import pygame

class Character:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.prev_x = 0
        self.prev_y = 0
        self.step = 40

    def step_left(self):
        if self.x - self.step >= 0: 
            self.save_pos()
            self.x -= self.step

    def step_right(self):
        if self.x + self.step < self.surface.get_width() - 1:
            self.save_pos()
            self.x += self.step

    def step_up(self):
        if self.y - self.step >= 0:
            self.save_pos()
            self.y -= self.step

    def step_down(self):
        if self.y + self.step < self.surface.get_height() - 1:
            self.save_pos() 
            self.y += self.step

    def check_hit(self, obstacle):
        hit = (self.x == obstacle.x) and (self.y == obstacle.y)
        return hit

    def save_pos(self):
        self.prev_x = self.x
        self.prev_y = self.y

    def step_back(self):
        self.x = self.prev_x
        self.y = self.prev_y
