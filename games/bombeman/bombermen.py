import pygame
import tkinter
from tkinter import messagebox
import random
import player
import bomb
import labyrinth
import brick

FPS = 30

pygame.init()
pygame.display.set_caption('Bomberman')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

# TODO: skins
bomber = player.Player((0, 255, 0), surface)
bombs = []
bricks = []
laby = labyrinth.Labyrinth((200, 200, 200))

for i in range(0, 150):
    x = random.randint(0, 17) * 40
    y = random.randint(0, 17) * 40
    br = brick.Brick(x, y, (200, 200, 200))
    bricks.append(br)

def game_over():
    tkinter.messagebox.showinfo('GAME OVER','OK')


running = True

while running:
    clock.tick(FPS)
    events = pygame.event.get()

    player_x = bomber.x
    player_y = bomber.y

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bomber.step_left()
            elif event.key == pygame.K_d:
                bomber.step_right()
            elif event.key == pygame.K_w:
                bomber.step_up()
            elif event.key == pygame.K_s:
                bomber.step_down()
            elif event.key == pygame.K_SPACE:
                b = bomb.Bomb(bomber.x, bomber.y, (127, 127, 127), (225, 0, 0))
                bombs.append(b)
    
    
    surface.fill((0, 0, 0))

    laby.draw(surface)


    exploded_bricks = [] 

    for brick in bricks:
        brick.draw(surface)
        if bomber.check_hit(brick):
            bomber.x = player_x
            bomber.y = player_y
        for b in bombs:
            if b.check_hit(brick):
                exploded_bricks.append(brick)
    bricks = list(set(bricks) - set(exploded_bricks))
    
    exploded_bombs = []

    for b in bombs:
        if b.tick():
            b.draw(surface)
        else:
            exploded_bombs.append(b)
        if bomber.check_hit(b):
            bomber.x = player_x
            bomber.y = player_y
        if b.check_hit(bomber):
            running = False
            game_over()
            break       
    bombs = list(set(bombs) - set(exploded_bombs))
    
    
    bomber.draw()

    pygame.display.update()

pygame.quit()