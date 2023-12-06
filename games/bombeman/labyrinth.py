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
        for x in range(17):
            for y in range(17):
                if x < 2 and y < 2:
                    continue
                brick_probability = random.randint(0,289)
                unbreaking_probabilty = random.randint(0, 100)
                if brick_probability <= 150:
                    if unbreaking_probabilty <= 15:
                        br = brick.UnbreakingBrick(surface, x*40, y*40)
                        bricks.append(br)
                    else:
                        br = brick.Brick(surface, x*40, y*40)
                        bricks.append(br)

        return bricks