import pygame
import character

BRICK_SIZE = 40

class Brick(character.GameObject):

    def __init__(self, surface,  x, y):
        super().__init__(surface)
        self.x = x
        self.y = y
        self.strength = 10
        self.set_skin('./images/brick_1.png')

class UnbreakingBrick(Brick):

    def __init__(self, surface, x, y):
        super().__init__(surface, x, y)
        self.strength = 100
        self.set_skin('./images/brick_2.png')