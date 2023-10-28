import pygame
import random
import brick

class Labyrinth:

    def __init__(self, color):
        self.color = color

    def draw(self, surface):
        step = 40
        x = 0
        y = surface.get_height()
        while x < surface.get_width():
            pygame.draw.line(surface, self.color, (x, 0), (x, y))
            x += step

        y = 0
        x = surface.get_width()
        while y < surface.get_height():
            pygame.draw.line(surface, self.color, (0, y), (x, y))
            y += step

    def fill_with_bricks(self, curr_skin):
        bricks = []
        for i in range(0, 175):
            x = random.randint(0, 17) * 40
            y = random.randint(0, 17) * 40
            if x < 80 and y < 80:
                continue
            br = brick.Brick(x, y, curr_skin.name)
            bricks.append(br)
        return bricks