import pygame
import character
import random
import labyrinth

class Monster(character.Character):
    def __init__(self, surface):
        super().__init__(surface)
        (x, y) = labyrinth.generate_coordinates(5)
        print('monster', x, y)
        self.x = x
        self.y = y
        self.sec_counter = 0
        self.ghost = False
        self.color = (255, 0, 0)

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
    def __init__(self, surface):
        super().__init__(surface)
        self.ghost = True
        self.color = (204, 255, 255)

    def check_hit(self, obstacle):
        return False