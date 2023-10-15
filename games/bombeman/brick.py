import pygame

BRICK_SIZE = 40

class Brick:

    def __init__(self, x, y, skin_name):
        self.x = x
        self.y = y
        self.set_skin(skin_name)

    def draw(self, surface):
        surface.blit(self.img, self.rect)
    
    def set_skin(self, skin_name):
        self.img = pygame.image.load(f'./images/brick_{skin_name}.png')
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = pygame.transform.rotozoom(self.img, 0, 40 / self.rect.width)
