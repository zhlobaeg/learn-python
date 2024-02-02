import pygame
import tkinter
from tkinter import messagebox
import platform

def game_over():
    tkinter.messagebox.showinfo('game over','вы продали почку')

FPS = 30

pygame.init()
pygame.display.set_caption('Falling rocks')
surface = pygame.display.set_mode((760, 821))
clock = pygame.time.Clock()

running = True

platf = platform.Platform(surface, 380, 750)

while running:
    clock.tick(FPS)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                platf.direction = platform.Direction.left
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                platf.direction = platform.Direction.right
        if event.type == pygame.KEYUP:
            platf.direction = None


    surface.fill((0,0,0))
    platf.moving()
    platf.draw()

    pygame.display.update()