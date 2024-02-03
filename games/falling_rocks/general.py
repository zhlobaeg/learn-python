import pygame
import tkinter
from tkinter import messagebox
import platform
import rocks

def game_over():
    tkinter.messagebox.showinfo('game over','вы продали почку')

FPS = 30

pygame.init()
pygame.display.set_caption('Falling rocks')
surface = pygame.display.set_mode((760, 1000))
clock = pygame.time.Clock()

running = True

platf = platform.Platform(surface, 380, 750)
stones = []

difficult = int(input('1- нормальный режим/ 2- сложный режим/ 3- невозможно: '))
if difficult == 1:
    for i in range(5):
        stone = rocks.Rock(surface, 0, 0)
        stone.random_spawn()
        stones.append(stone)
elif difficult == 2:
    for i in range(10):
        stone = rocks.Rock(surface, 0, 0)
        stone.random_spawn()
        stones.append(stone)
elif difficult == 3:
    for i in range(15):
        stone = rocks.Rock(surface, 0, 0)
        stone.random_spawn()
        stones.append(stone)

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
    for stone in stones:
        if stone.step < 30:
            stone.step += 0.01
            print(stone.step)
        elif stone.step == 30:
            tkinter.messagebox.showinfo('gg','вы получили 3ю почку')
            running = False

        stone.move()
        stone.draw()
        if platf.check_hit(stone):
            game_over()
            running = False

    pygame.display.update()