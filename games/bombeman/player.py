import pygame

class Player:
    def __init__(self, color, surface):
        self.color = color
        self.x = 20
        self.y = 20
        self.step = 40
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), 20)

    def step_left(self):
        if self.x - self.step > 0: 
            self.x -= self.step

    def step_right(self):
        if self.x + self.step < self.surface.get_width():
            self.x += self.step

    def step_up(self):
        if self.y - self.step > 0:
            self.y -= self.step

    def step_down(self):
        if self.y + self.step < self.surface.get_height(): 
            self.y += self.step

    def check_hit(self, brick):
        hit = (self.x == brick.x + 20) and (self.y == brick.y + 20)
        return hit
    
    def check_hit_bomb(self, bomb):
        hit = (self.x == bomb.x) and (self.y == bomb.y)
        return hit