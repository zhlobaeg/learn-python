import pygame
from character import Character

class Player(Character):
    def __init__(self, surface):
        super().__init__(surface)
        self.set_image('./images/player_1.png')
        self.carry_pickaxe = True
        self.carry_shieldy = True
        self.can_place_g_bomb = False