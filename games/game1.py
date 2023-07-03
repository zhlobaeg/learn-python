import pygame 

FPS = 2
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)

pygame.init()
surface = pygame.display.set_mode((800, 600))
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

    surface.fill(GREY)
    is_even = num_steps % 2 == 0
    if is_even:
        pygame.draw.rect(surface, RED, (300, 200, 200, 200))
    else:
        pygame.draw.rect(surface, BLUE, (300, 200, 200, 200))

    pygame.draw.circle(surface, GREEN, (500, 300), 50)
    pygame.display.update()
    num_steps += 1
    pygame.display.set_caption(f'My game. Step {num_steps}')