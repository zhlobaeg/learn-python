import pygame

LIFE_TIME = 90
BLAST_TIME = 15
BOMB_SIZE = 20

class Bomb:
    def __init__(self, x, y, color, blast_color):
        self.x = x
        self.y = y
        self.color = color
        self.blast_color = blast_color
        self.counter = LIFE_TIME

    def draw(self, surface):
        curr_color = self.color
        if self.counter < 0:
            curr_color = self.blast_color
        pygame.draw.circle(surface, curr_color, (self.x, self.y), BOMB_SIZE)    
    
    def tick(self):
        self.counter -= 1
        return self.counter > -BLAST_TIME    