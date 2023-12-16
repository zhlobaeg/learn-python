import character
import random

def chance_of_dropping():
        #number = random.randint(1, 5)
        #return numner == 3
        return True

class Pickaxe(character.GameObject):
    def __init__(self, surface,  x, y):
        super().__init__(surface)
        self.x = x
        self.y = y
        self.set_image('./images/pickaxe.png')
        self.durability = 6

    def hit(self):
        self.durability -= 1
        return self.durability > 0