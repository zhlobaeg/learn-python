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
        pygame.draw.circle(surface, curr_color, (self.x + 20, self.y + 20), BOMB_SIZE)    
    
    def tick(self):
        self.counter -= 1
        return self.counter > -BLAST_TIME  

    def check_hit(self, brick):
        boom = self.counter < 0 
        hit = (self.x == brick.x ) and (self.y == brick.y)
        hit_bottom = (self.x == brick.x ) and (self.y == brick.y - 40)
        hit_top = (self.x == brick.x) and (self.y == brick.y + 40)
        hit_left = (self.x == brick.x - 40) and (self.y == brick.y)
        hit_right = (self.x == brick.x + 40) and (self.y == brick.y)
        return boom and (hit or hit_top or hit_bottom or hit_left or hit_right)
    
