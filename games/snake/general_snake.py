import pygame
import tkinter
from tkinter import messagebox
import field
import snake
import food

FPS = 3
i = 0

pygame.init()
pygame.display.set_caption('Snake')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

running = True

snaky = snake.Snake(surface, 0, 0)
foood = food.Food(surface)

while running:
    clock.tick(FPS)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                snaky.direction = snake.Direction.left
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                snaky.direction = snake.Direction.right
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                snaky.direction = snake.Direction.up
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                snaky.direction = snake.Direction.down

    surface.fill((0, 0, 0))
    field.draw(surface)

    if snaky.check_hit(foood):
        foood = food.Food(surface)
        snaky.counter += 1
        print(snaky.counter)
        snaky.grow()

    foood.draw()
    snaky.move()
    snaky.draw()

    pygame.display.update()