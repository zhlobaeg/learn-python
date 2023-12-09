import pygame
from character import Character

class Player(Character):
    def __init__(self, skin_name, surface):
        super().__init__(surface)
        self.set_skin(f'./images/player_{skin_name}.png')
        self.carry_pickaxe = True
        self.can_place_g_bomb = False