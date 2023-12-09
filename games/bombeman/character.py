import pygame

class GameObject:
    def __init__(self, surface):
        self.surface = surface
        self.x = 0
        self.y = 0
        self.img = None
        self.rect = None
        self.color = (73, 200, 158)

    def set_skin(self, img_file):
        self.img = pygame.image.load(img_file)
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = pygame.transform.rotozoom(self.img, 0, 40 / self.rect.width)

    def draw(self):       
        if self.img:
            self.rect.x = self.x
            self.rect.y = self.y
            self.surface.blit(self.img, self.rect)
        else:
            pygame.draw.circle(self.surface, self.color, (self.x + 20, self.y + 20), 20)

    def place(self, x, y):
        self.x = x
        self.y = y

class Character(GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.prev_x = 0
        self.prev_y = 0
        self.step = 40

    def step_left(self):
        if self.x - self.step >= 0: 
            self.save_pos()
            self.x -= self.step

    def step_right(self):
        if self.x + self.step < self.surface.get_width() - 1:
            self.save_pos()
            self.x += self.step

    def step_up(self):
        if self.y - self.step >= 0:
            self.save_pos()
            self.y -= self.step

    def step_down(self):
        if self.y + self.step < self.surface.get_height() - 1:
            self.save_pos() 
            self.y += self.step

    def check_hit(self, obstacle):
        if obstacle is None:
            return False
        hit = (self.x == obstacle.x) and (self.y == obstacle.y)
        return hit

    def save_pos(self):
        self.prev_x = self.x
        self.prev_y = self.y

    def step_back(self):
        self.x = self.prev_x
        self.y = self.prev_y