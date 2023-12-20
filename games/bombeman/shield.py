import pygame
import character
import player

class Shield(character.GameObject):
    def __init__(self, surface, x, y):
        super().__init__(surface)
        self.durability = 2
        self.x = x
        self.y = y
        self.set_image('./images/shield.png')

    def protection(self):
        return self.durability > 0


    def damage(self):
        print(self.durability)
        self.durability -= 1