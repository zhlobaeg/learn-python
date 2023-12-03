import character

class Pickaxe(character.GameObject):
    def __init__(self, surface,  x, y):
        super().__init__(surface)
        self.x = x
        self.y = y