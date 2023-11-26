import pygame
import character
import random

class Monster(character.Character):
    def __init__(self, surface, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = surface
        self.sec_counter = 0
        self.immortal = False

    def draw(self):
        pygame.draw.circle(self.surface, (255, 0, 0), (self.x + 20, self.y + 20), 20)

    def walk(self):
        self.sec_counter += 1
        if self.sec_counter == 50:
            self.sec_counter = 0

            direction = random.randint(1, 4)

            if direction == 1:
                self.step_left()
            elif direction == 2:
                self.step_up()
            elif direction == 3:
                self.step_right()
            elif direction == 4:
                self.step_down()    

    def step_back(self):
        super().step_back()
        self.sec_counter = 49

class GhostMonster(Monster):
    def __init__(self, surface, x, y):
        super().__init__(surface, x, y)
        self.immortal = True

    def draw(self):
        pygame.draw.circle(self.surface, (204, 255, 255), (self.x + 20, self.y + 20), 20)

    def check_hit(self, obstacle):
        return False