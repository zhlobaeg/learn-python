import pygame
import character
import labyrinth

class Generator(character.GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.color = (255, 255, 0)
        # (x, y) = labyrinth.generate_coordinates(8)
        self.x = 5 * 40
        self.y = 5 * 40

        