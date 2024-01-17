import pygame
import character
import player
import pickaxe
import random

def chance_of_dropping():
        number = random.randint(1, 3)
        return number == 2

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