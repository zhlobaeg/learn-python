import character

class Pickaxe(character.GameObject):
    def __init__(self, surface,  x, y):
        super().__init__(surface)
        self.x = x
        self.y = y
        self.durability = 5

    def hit(self):
        self.durability -= 1
        return self.durability > 0