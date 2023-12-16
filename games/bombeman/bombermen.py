import pygame
import tkinter
from tkinter import messagebox
import random
import player
import bomb
import labyrinth
import brick
import monster
import pickaxe
import top_secret
import generator

FPS = 50

pygame.init()
pygame.display.set_caption('Bomberman')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

top_secret.super_secret()
top_secret.SUS()

# игрок и кирка
bomber = player.Player(surface)
pick = None
if pickaxe.chance_of_dropping():
    pick = pickaxe.Pickaxe(surface, bomber.x, bomber.y)
    bomber.carry_pickaxe = True
else:
    bomber.carry_pickaxe = False
bombs = []

# генератор
gener = generator.Generator(surface)

# лабиринт и кирпичи
laby = labyrinth.Labyrinth()
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
    if gener.check_hit(brick):
        exploded_bricks.append(brick)

bricks = list(set(bricks) - set(exploded_bricks))

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
                if not bomber.carry_pickaxe:
                    b = bomb.Bomb(bomber.x, bomber.y)
                    bombs.append(b)
                b = bomb.Bomb(g_mons.x, g_mons2.y)
                bombs.append(b)
                b = bomb.Bomb(g_mons2.x, g_mons.y)
                bombs.append(b)
            elif event.key == pygame.K_e and not bomber.carry_pickaxe and bomber.can_place_g_bomb:
                g_b = bomb.GhostBomb(surface, bomber.x, bomber.y)
                bombs.append(g_b)
            elif event.key == pygame.K_f and bomber.check_hit(pick):
                bomber.carry_pickaxe = not bomber.carry_pickaxe

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
        if mons != mons1:
            mons.walk()
        
    # перерисовка лабиринта
    surface.fill((0, 0, 0))
    laby.draw(surface)

    # check_hit с кирпичами и взрыв кирпичей
    exploded_bricks = [] 

    for brick in bricks:
        brick.draw()
        if bomber.check_hit(brick):
            if pick and brick.strength < 20 and pick.hit():
                exploded_bricks.append(brick)
            else:
                bomber.step_back()
        for mons in monsters:
            if mons.check_hit(brick):
                mons.step_back()
        for b in bombs:
            if b.check_hit(brick) and brick.strength < 20:
                exploded_bricks.append(brick)           

    bricks = list(set(bricks) - set(exploded_bricks))

    # смерть игрока от монстров
    for mons in monsters:
        if bomber.check_hit(mons) and mons != mons1:
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
        if b.check_hit(bomber) or b.check_hit(mons1):
            running = False
            game_over()
            break
        for mons in monsters:
            if b.check_hit(mons) and (b.ghost == mons.ghost):
                exploded_monsters.append(mons)
            if mons.check_hit(b):
                mons.step_back()

    # check_hit
    if mons.check_hit(gener):
        mons.step_back()
                
    bombs = list(set(bombs) - set(exploded_bombs))
    monsters = list(set(monsters) - set(exploded_monsters))

    # проверка что игрок нашёл генератор
    if gener.check_hit(bomber):
        bomber.can_place_g_bomb= True
    
    # отрисовка
    bomber.draw()
    if bomber.carry_pickaxe:
        pick.place(bomber.x, bomber.y)
    if pick :
        pick.draw()
    for mons in monsters:
        mons.draw()

    if not bomber.can_place_g_bomb:
        gener.draw()

    pygame.display.update()

pygame.quit()