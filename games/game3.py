import pygame

FPS = 60
GREEN = (0, 255, 127)
BLACK = (0, 0, 0)

pygame.init()
surface = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

pygame.display.set_caption('My Game 3')

running = True
x = 400
y = 350
speed_x = 0
speed_y = 0
LEFT = 50
RIGHT = 750
TOP = 50
BUTTOM = 650

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                speed_x = -10
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                speed_x = 10
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                speed_y = -10
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                speed_y = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                speed_x = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                speed_y = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                speed_y = 0

    surface.fill(BLACK)
    x += speed_x
    y += speed_y
    if x <= LEFT:
        x = LEFT
    elif x >= RIGHT:
        x = RIGHT
    if y <= TOP:
        y = TOP
    elif y >= BUTTOM:
        y = BUTTOM
    pygame.draw.circle(surface, GREEN, (x, y), 50)

    pygame.display.update()