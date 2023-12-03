import pygame
import random
import brick

def generate_coordinates(free_cells = 2):
        x = random.randint(0, 17) * 40
        y = random.randint(0, 17) * 40
        free = free_cells * 40
        if x < free and y < free:
            return generate_coordinates(free_cells)
        return (x, y)

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

    def fill_with_bricks(self, surface):
        bricks = []
        for i in range(0, 225):
            (x, y) = generate_coordinates()
            br = brick.Brick(surface, x, y)
            bricks.append(br)

        for i in range(random.randint(10, 30)):
            (x, y) = generate_coordinates()
            br = brick.UnbreakingBrick(surface, x, y)
            bricks.append(br)

        return bricks