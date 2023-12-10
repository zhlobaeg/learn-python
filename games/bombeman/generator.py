import pygame
import character
import labyrinth

class Generator(character.GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.set_skin(f'./images/generator.png')
        (x, y) = labyrinth.generate_coordinates(8)
        self.x = x
        self.y = y

        