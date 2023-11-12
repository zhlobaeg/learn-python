import pygame
import character

class Monster(character.Character):
    def __init__(self, surface, x, y):
        print('djk')
        super().__init__()
        self.x = x
        self.y = y
        self.surface = surface
        self.alive = True

    def draw(self):
        if self.alive:
            pygame.draw.circle(self.surface, (255, 0, 0), (self.x + 20, self.y + 20), 20)

    def delete(self):
        self.alive = False
        self.x = -100