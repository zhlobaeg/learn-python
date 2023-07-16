import pygame

class Player:
    def __init__(self, skin_name, surface):
        self.x = 0
        self.y = 0
        self.step = 40
        self.surface = surface
        self.set_skin(skin_name)

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        surface.blit(self.img, self.rect)

    def step_left(self):
        if self.x - self.step >= 0: 
            self.x -= self.step

    def step_right(self):
        if self.x + self.step < self.surface.get_width() - 1:
            self.x += self.step

    def step_up(self):
        if self.y - self.step >= 0:
            self.y -= self.step

    def step_down(self):
        if self.y + self.step < self.surface.get_height() - 1: 
            self.y += self.step

    def check_hit(self, brick):
        hit = (self.x == brick.x) and (self.y == brick.y)
        return hit
    
    def set_skin(self, skin_name):
        self.img = pygame.image.load(f'./images/player_{skin_name}.jpg')
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = pygame.transform.rotozoom(self.img, 0, 40 / self.rect.width)