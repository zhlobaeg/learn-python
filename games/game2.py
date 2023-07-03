import pygame

FPS = 15
PURPLE =(148, 0, 211)
GREEN = (0, 255, 127)
BLACK = (0, 0, 0)

pygame.init()
surface = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.display.set_caption('My game2')

running = True

to_circle_x = 850
from_circle_x = -50
circle_x = from_circle_x
circle_speed = 0

to_rect_y = 850
from_rect_y = -50
rect_y = from_rect_y
rect_speed = 0

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    surface.fill(BLACK)
    pygame.draw.circle(surface, GREEN, (circle_x, 400), 50)
    circle_x += circle_speed
    if circle_x >= to_circle_x:
        circle_x = from_circle_x
    circle_speed += 2
    if circle_speed >= 150:
        circle_speed = 150

    pygame.draw.rect(surface, PURPLE, (400, rect_y, 50, 50))
    rect_y += rect_speed
    if rect_y >= to_rect_y:
        rect_y = from_rect_y
    rect_speed += 1
    if rect_speed >= 200:
        rect_speed = 200

    pygame.display.update()