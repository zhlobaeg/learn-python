import pygame

class Player:
    def __init__(self, color, surface):
        self.color = color
        self.x = 0
        self.y = 0
        self.step = 40
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x + 20, self.y + 20), 20)

    def step_left(self):
        if self.x - self.step >= 0: 
            self.x -= self.step

    def step_right(self):
        # TODO: взять правую границу у объекта labyrinth
        if self.x + self.step < self.surface.get_width() - 1:
            self.x += self.step

    def step_up(self):
        if self.y - self.step >= 0:
            self.y -= self.step

    def step_down(self):
        # TODO: взять нижнюю границу у объекта labyrinth
        if self.y + self.step < self.surface.get_height() - 1: 
            self.y += self.step

    def check_hit(self, brick):
        hit = (self.x == brick.x) and (self.y == brick.y)
        return hit
    