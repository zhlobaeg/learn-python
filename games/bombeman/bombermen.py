import pygame
import tkinter
from tkinter import messagebox
import random
import player
import bomb
import labyrinth
import brick
import skin
import monster
import pickaxe

FPS = 50

pygame.init()
pygame.display.set_caption('Bomberman')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

curr_skin = skin.skin_1

# игрок и кирка
bomber = player.Player(curr_skin.name, surface)
pick = pickaxe.Pickaxe(surface, bomber.x, bomber.y)
bombs = []

# лабиринт и кирпичи
laby = labyrinth.Labyrinth(curr_skin.brick_color)
bricks = laby.fill_with_bricks(surface)

# монстры
monsters = []
for i in range(5):
    mons = monster.Monster(surface)
    monsters.append(mons)
g_mons = monster.GhostMonster(surface)
g_mons2 = monster.GhostMonster(surface)
monsters.append(g_mons)
monsters.append(g_mons2)
mons1 = monsters[0]

# удаление кирпичей на монстрах
exploded_bricks = []

for brick in bricks:
    for mons in monsters:
        if mons.check_hit(brick):
            exploded_bricks.append(brick)

bricks = list(set(bricks) - set(exploded_bricks))


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

def game_over():
    tkinter.messagebox.showinfo('ласт кристмас','сдох)')


running = True

while running:
    clock.tick(FPS)
    events = pygame.event.get()

    # нажатия на клавиатуре
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
                b = bomb.Bomb(bomber.x, bomber.y, curr_skin.name)
                bombs.append(b)
                b = bomb.Bomb(g_mons.x, g_mons2.y, curr_skin.name)
                bombs.append(b)
                b = bomb.Bomb(g_mons2.x, g_mons.y, curr_skin.name)
                bombs.append(b)
            elif event.key == pygame.K_e:
                g_b = bomb.GhostBomb(surface, bomber.x, bomber.y, curr_skin.name)
                bombs.append(g_b)
            elif event.key == pygame.K_1:
                change_skin(1)
            elif event.key == pygame.K_2:
                change_skin(2)
            elif event.key == pygame.K_3:
                change_skin(3)

            if event.key == pygame.K_LEFT:
                mons1.step_left()
            elif event.key == pygame.K_RIGHT:
                mons1.step_right()
            elif event.key == pygame.K_UP:
                mons1.step_up()
            elif event.key == pygame.K_DOWN:
                mons1.step_down()

    # монстры ходят по лабиринту
    for mons in monsters:
        mons.walk()
        
    # перерисовка лабиринта
    surface.fill(curr_skin.background_color)
    laby.draw(surface)

    # check_hit с кирпичами и взрыв кирпичей
    exploded_bricks = [] 

    for brick in bricks:
        brick.draw()
        if bomber.check_hit(brick):
            bomber.step_back()
            if pick and brick.strength < 20:
                exploded_bricks.append(brick)
        for mons in monsters:
            if mons.check_hit(brick):
                mons.step_back()
        for b in bombs:
            if b.check_hit(brick) and brick.strength < 20:
                exploded_bricks.append(brick)           

    bricks = list(set(bricks) - set(exploded_bricks))

    # смерть игрока от монстров
    for mons in monsters:
        if bomber.check_hit(mons):
            running = False
            game_over()
            break

    # бомба убивает монстров и игрока
    exploded_bombs = []
    exploded_monsters = []

    for b in bombs:
        if b.tick():
            b.draw(surface)
        else:
            exploded_bombs.append(b)
        if bomber.check_hit(b):
            bomber.step_back()
        if b.check_hit(bomber):
            running = False
            game_over()
            break
        for mons in monsters:
            if b.check_hit(mons) and (b.ghost == mons.ghost):
                exploded_monsters.append(mons)
            if mons.check_hit(b):
                mons.step_back()
                
    bombs = list(set(bombs) - set(exploded_bombs))
    monsters = list(set(monsters) - set(exploded_monsters))
    
    # отрисовка
    bomber.draw()
    pick.place(bomber.x, bomber.y)
    pick.draw()
    for mons in monsters:
        mons.draw()

    pygame.display.update()

pygame.quit()