import pygame
import character
import random
import labyrinth

class Monster(character.Character):
    def __init__(self, surface):
        super().__init__(surface)
        (x, y) = labyrinth.generate_coordinates(5)
        self.x = x
        self.y = y
        self.sec_counter = 0
        self.ghost = False
        self.set_image('./images/monster.png')
        self.wrong_moves = []
        self.directions = [1, 2, 3, 4]
        self.direction = None

    def walk(self):
        self.sec_counter += 1
        if self.sec_counter == 50:
            self.sec_counter = 0

            valid_directions = list(set(self.directions) - set(self.wrong_moves))  
            if valid_directions == []:
                self.wrong_moves = []
                self.direction = random.choice(self.directions)
            else:
                self.direction = random.choice(valid_directions)    

            if self.direction == 1:
                self.step_left()
            elif self.direction == 2:
                self.step_up()
            elif self.direction == 3:
                self.step_right()
            elif self.direction == 4:
                self.step_down() 
            self.wrong_moves = []   

    def step_back(self):
        super().step_back()
        self.sec_counter = 40
        self.wrong_moves.append(self.direction)
        self.walk()       

class GhostMonster(Monster):
    def __init__(self, surface):
        super().__init__(surface)
        self.ghost = True
        self.set_image('./images/ghost.png')

    def check_hit(self, obstacle):
        return False