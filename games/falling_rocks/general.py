import pygame
import tkinter
from tkinter import messagebox
import platform

def game_over():
    tkinter.messagebox.showinfo('game over','вы продали почку')

FPS = 50

pygame.init()
pygame.display.set_caption('Falling rocks')
surface = pygame.display.set_mode((760, 821))
clock = pygame.time.Clock()

running = True

platform = platform.Platform(surface, 380, 750)

while running:
    clock.tick(FPS)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                platform.step_left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                platform.step_right()

    surface.fill((0,0,0))
    platform.draw()

    pygame.display.update()