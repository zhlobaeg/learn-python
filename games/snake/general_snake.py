import pygame
import tkinter
from tkinter import messagebox
import field

FPS = 50

pygame.init()
pygame.display.set_caption('Snake')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(FPS)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

    surface.fill((0, 0, 0))
    field.draw(surface)

    pygame.display.update()