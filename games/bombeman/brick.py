import pygame

BRICK_SIZE = 40

class Brick:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None
        self.strength = 10
        self.set_skin('./images/brick_1.png')

    def draw(self, surface):
        surface.blit(self.img, self.rect)
    
    def set_skin(self, img_file):
        self.img = pygame.image.load(img_file)
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = pygame.transform.rotozoom(self.img, 0, 40 / self.rect.width)


class UnbreakingBrick(Brick):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.strength = 100
        self.set_skin('./images/brick_2.png')