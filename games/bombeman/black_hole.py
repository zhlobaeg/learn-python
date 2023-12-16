import pygame
import character
import labyrinth

class BlackHole(character.GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.set_image('./images/black_hole.png')
        (x, y) = labyrinth.generate_coordinates()
        self.x = x
        self.y = y