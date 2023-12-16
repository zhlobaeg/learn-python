import pygame
import character

class BlackHole(character.GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.set_image('./images/black_hole.png')