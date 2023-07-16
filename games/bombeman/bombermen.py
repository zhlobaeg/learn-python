import pygame
import tkinter
from tkinter import messagebox
import random
import player
import bomb
import labyrinth
import brick
import skin

FPS = 30

pygame.init()
pygame.display.set_caption('Bomberman')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

#TODO: звуки
#TODO: заменить картинки для игрока на png
#TODO: текстуры для бомб
curr_skin = skin.skin_1
bomber = player.Player(curr_skin.name, surface)
bombs = []
bricks = []
laby = labyrinth.Labyrinth(curr_skin.brick_color)

for i in range(0, 150):
    x = random.randint(0, 17) * 40
    y = random.randint(0, 17) * 40
    br = brick.Brick(x, y, curr_skin.name)
    bricks.append(br)


def change_skin(skin_number):
    global curr_skin
    global bricks
    if skin_number == 1:
        curr_skin = skin.skin_1
    elif skin_number == 2:
        curr_skin = skin.skin_2
    elif skin_number == 3:
        curr_skin = skin.skin_3
    bomber.set_skin(curr_skin.name)
    laby.color = curr_skin.brick_color
    for brick in bricks:
        brick.set_skin(curr_skin.name)

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
                b = bomb.Bomb(bomber.x, bomber.y, curr_skin.bomb_color, curr_skin.bomb_blast_color)
                bombs.append(b)
            elif event.key == pygame.K_1:
                change_skin(1)
            elif event.key == pygame.K_2:
                change_skin(2)
            elif event.key == pygame.K_3:
                change_skin(3)
        
    
    surface.fill(curr_skin.background_color)

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
    
    
    bomber.draw(surface)

    pygame.display.update()

pygame.quit()