import pygame

COLOR = (51, 51, 51)

def draw(surface):
    step = 40
    x = 0
    y = surface.get_height()
    while x < surface.get_width():
        pygame.draw.line(surface, COLOR, (x, 0), (x, y))
        x += step

    y = 0
    x = surface.get_width()
    while y < surface.get_height():
        pygame.draw.line(surface, COLOR, (0, y), (x, y))
        y += step