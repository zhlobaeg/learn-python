import pygame

FPS = 120
GREEN = (0, 255, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
surface = pygame.display.set_mode((800, 200))
clock = pygame.time.Clock()



running = True
num_steps = 0

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    surface.fill(BLACK)

    x = 0
    for i in range(80):
        color = BLACK
        active_circle = num_steps % 80
        if i == active_circle:
            color = RED
            pygame.draw.circle(surface, color, (x, 100), 50)
        x += 10

    num_steps += 1
    FPS -= 0.1
    if FPS <= 2:
        break
    pygame.display.set_caption(f'My Game 4 {FPS}')
    pygame.display.update()