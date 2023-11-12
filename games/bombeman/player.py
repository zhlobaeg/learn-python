import pygame
from character import Character

class Player(Character):
    def __init__(self, skin_name, surface):
        super().__init__()
        self.surface = surface
        self.set_skin(skin_name)

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.surface.blit(self.img, self.rect)
    
    def set_skin(self, skin_name):
        self.img = pygame.image.load(f'./images/player_{skin_name}.png')
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = pygame.transform.rotozoom(self.img, 0, 40 / self.rect.width)