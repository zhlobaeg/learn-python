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
import black_hole
import shield

FPS = 50

pygame.init()
pygame.display.set_caption('Bomberman')
surface = pygame.display.set_mode((721, 721))
clock = pygame.time.Clock()

top_secret.super_secret()

# игрок
bomber = player.Player(surface, 80, 80)

# щит и супер щит
shieldy = None
if shield.chance_of_dropping() and not bomber.carry_pickaxe:
    shieldy = shield.Shield(surface, 40, 40) 
    bomber.carry_shieldy = True
else:
    bomber.carry_shieldy = False

# кирка
pick = None
if pickaxe.chance_of_dropping() and not bomber.carry_shieldy:
    pick = pickaxe.Pickaxe(surface, bomber.x, bomber.y)
    bomber.carry_pickaxe = True
else:
    bomber.carry_pickaxe = False
bombs = []

#чёрные дыры
black_holes = []
for i in range(10):
    b_hole = black_hole.BlackHole(surface)
    black_holes.append(b_hole)

# генератор
gener = generator.Generator(surface)

# лабиринт и кирпичи
laby = labyrinth.Labyrinth()
bricks = laby.fill_with_bricks(surface)

# монстры
monsters = []
for i in range(10):
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
            elif event.key == pygame.K_f:
                if bomber.carry_pickaxe:
                    bomber.carry_pickaxe = False
                else:
                    if bomber.check_hit(pick):
                        bomber.carry_pickaxe = True

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
        if bomber.check_hit(brick):
            if bomber.carry_pickaxe and brick.strength < 20 and pick.hit():
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
    for mons in monsters:
        for b_hole in black_holes:
            if mons.check_hit(b_hole):
                mons.step_back()
            elif mons.check_hit(shieldy) and shieldy.protection():
                mons.step_back()
                shieldy.damage()

    for b_hole in black_holes:
        if mons1.check_hit(b_hole):
            mons1.step_back()
                
    bombs = list(set(bombs) - set(exploded_bombs))
    monsters = list(set(monsters) - set(exploded_monsters))

    # проверка что игрок нашёл генератор
    if gener.check_hit(bomber):
        bomber.can_place_g_bomb= True
    
    # отрисовка
    for b_hole in black_holes:
        b_hole.draw()

    for brick in bricks:
        brick.draw()

    bomber.draw()
    if bomber.carry_shieldy and shieldy.protection():
        shieldy.place(bomber.x, bomber.y)
        shieldy.draw()
    if bomber.carry_pickaxe:
        pick.place(bomber.x, bomber.y)
    if pick and pick.durability > 0:
        pick.draw()
    else:
        bomber.carry_pickaxe = False

    for mons in monsters:
        mons.draw()

    if not bomber.can_place_g_bomb:
        gener.draw()

    pygame.display.update()

    # смерть игрока
    for mons in monsters:
        if bomber.check_hit(mons) and mons != mons1 and not shieldy.protection():
            running = False
            game_over()

    for b_hole in black_holes:
        if bomber.check_hit(b_hole):
            running = False
            game_over()


pygame.quit()